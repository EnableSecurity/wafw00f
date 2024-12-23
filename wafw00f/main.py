#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

import csv
import io
import json
import logging
import os
import random
import re
import sys
import string
import urllib.parse
from collections import defaultdict
from optparse import OptionParser

from wafw00f import __license__, __version__
from wafw00f.lib.asciiarts import Color, randomArt
from wafw00f.lib.evillib import waftoolsengine
from wafw00f.manager import load_plugins
from wafw00f.wafprio import wafdetectionsprio


class WAFW00F(waftoolsengine):

    xsstring = r'<script>alert("XSS");</script>'
    sqlistring = r'UNION SELECT ALL FROM information_schema AND " or SLEEP(5) or "'
    lfistring = r'../../etc/passwd'
    rcestring = r'/bin/cat /etc/passwd; ping 127.0.0.1; curl google.com'
    xxestring = r'<!ENTITY xxe SYSTEM "file:///etc/shadow">]><pwn>&hack;</pwn>'

    def __init__(self, target='www.example.com', debuglevel=0, path='/',
                 followredirect=True, extraheaders={}, proxies=None, timeout=7):

        self.log = logging.getLogger('wafw00f')
        self.attackres = None
        waftoolsengine.__init__(self, target, debuglevel, path, proxies, followredirect, extraheaders, timeout)
        self.knowledge = {
            'generic': {
                'found': False,
                'reason': ''
            },
            'wafname': []
        }
        self.rq = self.normalRequest()

    def normalRequest(self):
        return self.Request()

    def customRequest(self, headers=None):
        return self.Request(
            headers=headers
        )

    def nonExistent(self):
        return self.Request(
            path=self.path + str(random.randrange(100, 999)) + '.html'
        )

    def xssAttack(self):
        return self.Request(
            path=self.path,
            params={
                create_random_param_name(): self.xsstring
            }
        )

    def xxeAttack(self):
        return self.Request(
            path=self.path,
            params={
                create_random_param_name(): self.xxestring
            }
        )

    def lfiAttack(self):
        return self.Request(
            path=self.path + self.lfistring
        )

    def centralAttack(self):
        return self.Request(
            path=self.path,
            params={
                create_random_param_name(): self.xsstring,
                create_random_param_name(): self.sqlistring,
                create_random_param_name(): self.lfistring
            }
        )

    def sqliAttack(self):
        return self.Request(
            path=self.path,
            params={
                create_random_param_name(): self.sqlistring
            }
        )

    def osciAttack(self):
        return self.Request(
            path=self.path,
            params= {
                create_random_param_name(): self.rcestring
            }
        )

    def performCheck(self, request_method):
        r = request_method()
        if r is None:
            raise RequestBlocked()
        return r, r.url

    # Most common attacks used to detect WAFs
    attcom = [xssAttack, sqliAttack, lfiAttack]
    attacks = [xssAttack, xxeAttack, lfiAttack, sqliAttack, osciAttack]

    def genericdetect(self):
        reason = ''
        reasons = ['Blocking is being done at connection/packet level.',
                   'The server header is different when an attack is detected.',
                   'The server returns a different response code when an attack string is used.',
                   'It closed the connection for a normal request.',
                   'The response was different when the request wasn\'t made from a browser.'
                ]
        try:
            # Testing for no user-agent response. Detects almost all WAFs out there.
            resp1, _ = self.performCheck(self.normalRequest)
            if 'User-Agent' in self.headers:
                self.headers.pop('User-Agent')  # Deleting the user-agent key from object not dict.
            resp3 = self.customRequest(headers=self.headers)
            if resp3 is not None and resp1 is not None:
                if resp1.status_code != resp3.status_code:
                    self.log.info('Server returned a different response when request didn\'t contain the User-Agent header.')
                    reason = reasons[4]
                    reason += '\r\n'
                    reason += 'Normal response code is "%s",' % resp1.status_code
                    reason += ' while the response code to a modified request is "%s"' % resp3.status_code
                    self.knowledge['generic']['reason'] = reason
                    self.knowledge['generic']['found'] = True
                    return True

            # Testing the status code upon sending a xss attack
            resp2, xss_url = self.performCheck(self.xssAttack)
            if resp1.status_code != resp2.status_code:
                self.log.info('Server returned a different response when a XSS attack vector was tried.')
                reason = reasons[2]
                reason += '\r\n'
                reason += 'Normal response code is "%s",' % resp1.status_code
                reason += ' while the response code to cross-site scripting attack is "%s"' % resp2.status_code
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return xss_url

            # Testing the status code upon sending a lfi attack
            resp2, lfi_url = self.performCheck(self.lfiAttack)
            if resp1.status_code != resp2.status_code:
                self.log.info('Server returned a different response when a directory traversal was attempted.')
                reason = reasons[2]
                reason += '\r\n'
                reason += 'Normal response code is "%s",' % resp1.status_code
                reason += ' while the response code to a file inclusion attack is "%s"' % resp2.status_code
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return lfi_url

            # Testing the status code upon sending a sqli attack
            resp2, sqli_url = self.performCheck(self.sqliAttack)
            if resp1.status_code != resp2.status_code:
                self.log.info('Server returned a different response when a SQLi was attempted.')
                reason = reasons[2]
                reason += '\r\n'
                reason += 'Normal response code is "%s",' % resp1.status_code
                reason += ' while the response code to a SQL injection attack is "%s"' % resp2.status_code
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return sqli_url

            # Checking for the Server header after sending malicious requests
            normalserver, attackresponse_server = '', ''
            response = self.attackres
            if 'server' in resp1.headers:
                normalserver = resp1.headers.get('Server')
            if response is not None and 'server' in response.headers:
                attackresponse_server = response.headers.get('Server')
            if attackresponse_server != normalserver:
                self.log.info('Server header changed, WAF possibly detected')
                self.log.debug('Attack response: %s' % attackresponse_server)
                self.log.debug('Normal response: %s' % normalserver)
                reason = reasons[1]
                reason += '\r\nThe server header for a normal response is "%s",' % normalserver
                reason += ' while the server header a response to an attack is "%s",' % attackresponse_server
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return True

        # If at all request doesn't go, press F
        except RequestBlocked:
            self.knowledge['generic']['reason'] = reasons[0]
            self.knowledge['generic']['found'] = True
            return True
        return False

    def matchHeader(self, headermatch, attack=False):
        if attack:
            r = self.attackres
        else:
            r = self.rq
        if r is None:
            return

        header, match = headermatch
        headerval = r.headers.get(header)
        if headerval:
            # set-cookie can have multiple headers, python gives it to us
            # concatinated with a comma
            if header == 'Set-Cookie':
                headervals = headerval.split(', ')
            else:
                headervals = [headerval]
            for headerval in headervals:
                if re.search(match, headerval, re.I):
                    return True
        return False

    def matchStatus(self, statuscode, attack=True):
        if attack:
            r = self.attackres
        else:
            r = self.rq
        if r is None:
            return
        if r.status_code == statuscode:
            return True
        return False

    def matchCookie(self, match, attack=False):
        return self.matchHeader(('Set-Cookie', match), attack=attack)

    def matchReason(self, reasoncode, attack=True):
        if attack:
            r = self.attackres
        else:
            r = self.rq
        if r is None:
            return
        # We may need to match multiline context in response body
        if str(r.reason) == reasoncode:
            return True
        return False

    def matchContent(self, regex, attack=True):
        if attack:
            r = self.attackres
        else:
            r = self.rq
        if r is None:
            return
        # We may need to match multiline context in response body
        if re.search(regex, r.text, re.I):
            return True
        return False

    wafdetections = dict()

    plugin_dict = load_plugins()
    result_dict = {}
    for plugin_module in plugin_dict.values():
        wafdetections[plugin_module.NAME] = plugin_module.is_waf
    # Check for prioritized ones first, then check those added externally
    checklist = wafdetectionsprio
    checklist += list(set(wafdetections.keys()) - set(checklist))

    def identwaf(self, findall=False):
        detected = list()
        try:
            self.attackres, xurl = self.performCheck(self.centralAttack)
        except RequestBlocked:
            return detected, None
        for wafvendor in self.checklist:
            self.log.info('Checking for %s' % wafvendor)
            if self.wafdetections[wafvendor](self):
                detected.append(wafvendor)
                if not findall:
                    break
        self.knowledge['wafname'] = detected
        return detected, xurl

def calclogginglevel(verbosity):
    default = 40  # errors are printed out
    level = default - (verbosity * 10)
    if level < 0:
        level = 0
    return level

def buildResultRecord(url, waf, evil_url=None):
    result = {}
    result['url'] = url
    if waf:
        result['detected'] = True
        if waf == 'generic':
            result['trigger_url'] = evil_url
            result['firewall'] = 'Generic'
            result['manufacturer'] = 'Unknown'
        else:
            result['trigger_url'] = evil_url
            result['firewall'] = waf.split('(')[0].strip()
            result['manufacturer'] = waf.split('(')[1].replace(')', '').strip()
    else:
        result['trigger_url'] = evil_url
        result['detected'] = False
        result['firewall'] = 'None'
        result['manufacturer'] = 'None'
    return result

def getTextResults(res=[]):
    # leaving out some space for future possibilities of newer columns
    # newer columns can be added to this tuple below
    keys = ('detected')
    res = [({key: ba[key] for key in ba if key not in keys}) for ba in res]
    rows = []
    for dk in res:
        p = [str(x) for _, x in dk.items()]
        rows.append(p)
    for m in rows:
        m[1] = '%s (%s)' % (m[1], m[2])
        m.pop()
    defgen = [
        (max([len(str(row[i])) for row in rows]) + 3)
        for i in range(len(rows[0]))
    ]
    rwfmt = ''.join(['{:>'+str(dank)+'}' for dank in defgen])
    textresults = []
    for row in rows:
        textresults.append(rwfmt.format(*row))
    return textresults

def create_random_param_name(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def disableStdOut():
    sys.stdout = None

def enableStdOut():
    sys.stdout = sys.__stdout__

def getheaders(fn):
    headers = {}
    if not os.path.exists(fn):
        logging.getLogger('wafw00f').critical('Headers file "%s" does not exist!' % fn)
        return
    with io.open(fn, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            _t = line.split(':', 2)
            if len(_t) == 2:
                h, v = map(lambda x: x.strip(), _t)
                headers[h] = v
    return headers

class RequestBlocked(Exception):
    pass

def main():
    parser = OptionParser(usage='%prog url1 [url2 [url3 ... ]]\r\nexample: %prog http://www.victim.org/')
    parser.add_option('-v', '--verbose', action='count', dest='verbose', default=0,
                      help='Enable verbosity, multiple -v options increase verbosity')
    parser.add_option('-a', '--findall', action='store_true', dest='findall', default=False,
                      help='Find all WAFs which match the signatures, do not stop testing on the first one')
    parser.add_option('-r', '--noredirect', action='store_false', dest='followredirect',
                      default=True, help='Do not follow redirections given by 3xx responses')
    parser.add_option('-t', '--test', dest='test', help='Test for one specific WAF')
    parser.add_option('-o', '--output', dest='output', help='Write output to csv, json or text file depending on file extension. For stdout, specify - as filename.',
                      default=None)
    parser.add_option('-f', '--format', dest='format', help='Force output format to csv, json or text.',
                      default=None)
    parser.add_option('-i', '--input-file', dest='input', help='Read targets from a file. Input format can be csv, json or text. For csv and json, a `url` column name or element is required.',
                      default=None)
    parser.add_option('-l', '--list', dest='list', action='store_true',
                      default=False, help='List all WAFs that WAFW00F is able to detect')
    parser.add_option('-p', '--proxy', dest='proxy', default=None,
                      help='Use an HTTP proxy to perform requests, examples: http://hostname:8080, socks5://hostname:1080, http://user:pass@hostname:8080')
    parser.add_option('--version', '-V', dest='version', action='store_true',
                      default=False, help='Print out the current version of WafW00f and exit.')
    parser.add_option('--headers', '-H', dest='headers', action='store', default=None,
                      help='Pass custom headers via a text file to overwrite the default header set.')
    parser.add_option('-T', '--timeout', dest='timeout', action='store', default=7, type=int,
                      help='Set the timeout for the requests.')
    parser.add_option('--no-colors', dest='colors', action='store_false',
                      default=True, help='Disable ANSI colors in output.')

    options, args = parser.parse_args()

    logging.basicConfig(level=calclogginglevel(options.verbose))
    log = logging.getLogger('wafw00f')
    if options.output == '-':
        disableStdOut()

    # Windows based systems do not support ANSI sequences,
    # hence not displaying them.
    if not options.colors or 'win' in sys.platform:
        Color.disable()

    print(randomArt())
    (W,Y,G,R,B,C,E) = Color.unpack()

    if options.list:
        print('[+] Can test for these WAFs:\r\n')
        try:
            m = [i.replace(')', '').split(' (') for i in wafdetectionsprio]
            print(R+'  WAF Name'+' '*24+'Manufacturer\n  '+'-'*8+' '*24+'-'*12+'\n')
            max_len = max(len(str(x)) for k in m for x in k)
            for inner in m:
                first = True
                for elem in inner:
                    if first:
                        text = Y+'  {:<{}} '.format(elem, max_len+2)
                        first = False
                    else:
                        text = W+'{:<{}} '.format(elem, max_len+2)
                    print(text, E, end='')
                print()
            sys.exit(0)
        except Exception:
            return
    if options.version:
        print('[+] The version of WAFW00F you have is %sv%s%s' % (B, __version__, E))
        print('[+] WAFW00F is provided under the %s%s%s license.' % (C, __license__, E))
        return
    extraheaders = {}
    if options.headers:
        log.info('Getting extra headers from %s' % options.headers)
        extraheaders = getheaders(options.headers)
        if extraheaders is None:
            parser.error('Please provide a headers file with colon delimited header names and values')
    if len(args) == 0 and not options.input:
        parser.error('No test target specified.')
    #check if input file is present
    if options.input:
        log.debug('Loading file "%s"' % options.input)
        try:
            if options.input.endswith('.json'):
                with open(options.input) as f:
                    try:
                        urls = json.loads(f.read())
                    except json.decoder.JSONDecodeError:
                        log.critical('JSON file %s did not contain well-formed JSON', options.input)
                        sys.exit(1)
                log.info('Found: %s urls to check.' %(len(urls)))
                targets = [ item['url'] for item in urls ]
            elif options.input.endswith('.csv'):
                columns = defaultdict(list)
                with open(options.input) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        for (k,v) in row.items():
                            columns[k].append(v)
                targets = columns['url']
            else:
                with open(options.input) as f:
                    targets = [x for x in f.read().splitlines()]
        except FileNotFoundError:
            log.error('File %s could not be read. No targets loaded.', options.input)
            sys.exit(1)
    else:
        targets = args
    results = []
    for target in targets:
        if not target.startswith('http'):
            log.info('The url %s should start with http:// or https:// .. fixing (might make this unusable)' % target)
            target = 'https://' + target
        print('[*] Checking %s' % target)
        pret = urllib.parse.urlparse(target)
        if pret is None:
            log.critical('The url %s is not well formed' % target)
            sys.exit(1)
        log.info('starting wafw00f on %s' % target)
        proxies = dict()
        if options.proxy:
            proxies = {
                'http': options.proxy,
                'https': options.proxy,
            }
        attacker = WAFW00F(target, debuglevel=options.verbose, path=pret.path,
                    followredirect=options.followredirect, extraheaders=extraheaders,
                        proxies=proxies, timeout=options.timeout)
        if attacker.rq is None:
            log.error('Site %s appears to be down' % pret.hostname)
            continue
        if options.test:
            if options.test in attacker.wafdetections:
                waf = attacker.wafdetections[options.test](attacker)
                if waf:
                    print('[+] The site %s%s%s is behind %s%s%s WAF.' % (B, target, E, C, options.test, E))
                else:
                    print('[-] WAF %s was not detected on %s' % (options.test, target))
            else:
                print('[-] WAF %s was not found in our list\r\nUse the --list option to see what is available' % options.test)
            return
        waf, xurl = attacker.identwaf(options.findall)
        log.info('Identified WAF: %s' % waf)
        if len(waf) > 0:
            for i in waf:
                results.append(buildResultRecord(target, i, xurl))
            print('[+] The site %s%s%s is behind %s%s%s WAF.' % (B, target, E, C, (E+' and/or '+C).join(waf), E))
        if (options.findall) or len(waf) == 0:
            print('[+] Generic Detection results:')
            generic_url = attacker.genericdetect()
            if generic_url:
                log.info('Generic Detection: %s' % attacker.knowledge['generic']['reason'])
                print('[*] The site %s seems to be behind a WAF or some sort of security solution' % target)
                print('[~] Reason: %s' % attacker.knowledge['generic']['reason'])
                results.append(buildResultRecord(target, 'generic', generic_url))
            else:
                print('[-] No WAF detected by the generic detection')
                results.append(buildResultRecord(target, None, None))
        print('[~] Number of requests: %s' % attacker.requestnumber)
    #print table of results
    if len(results) > 0:
        log.info('Found: %s matches.' % (len(results)))
    if options.output:
        if options.output == '-':
            enableStdOut()
            if options.format == 'json':
                json.dump(results, sys.stdout, indent=2, sort_keys=True)
            elif options.format == 'csv':
                csvwriter = csv.writer(sys.stdout, delimiter=',', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                count = 0
                for result in results:
                    if count == 0:
                        header = result.keys()
                        csvwriter.writerow(header)
                        count += 1
                    csvwriter.writerow(result.values())
            else:
                print(os.linesep.join(getTextResults(results)))
        elif options.output.endswith('.json'):
            log.debug('Exporting data in json format to file: %s' % (options.output))
            with open(options.output, 'w') as outfile:
                json.dump(results, outfile, indent=2, sort_keys=True)
        elif options.output.endswith('.csv'):
            log.debug('Exporting data in csv format to file: %s' % (options.output))
            with open(options.output, 'w') as outfile:
                csvwriter = csv.writer(outfile, delimiter=',', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                count = 0
                for result in results:
                    if count == 0:
                        header = result.keys()
                        csvwriter.writerow(header)
                        count += 1
                    csvwriter.writerow(result.values())
        else:
            log.debug('Exporting data in text format to file: %s' % (options.output))
            if options.format == 'json':
                with open(options.output, 'w') as outfile:
                    json.dump(results, outfile, indent=2, sort_keys=True)
            elif options.format == 'csv':
                with open(options.output, 'w') as outfile:
                    csvwriter = csv.writer(outfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
                    count = 0
                    for result in results:
                        if count == 0:
                            header = result.keys()
                            csvwriter.writerow(header)
                            count += 1
                        csvwriter.writerow(result.values())
            else:
                with open(options.output, 'w') as outfile:
                    outfile.write(os.linesep.join(getTextResults(results)))

if __name__ == '__main__':
    version_info = sys.version_info
    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 6):
        sys.stderr.write('Your version of python is way too old... please update to 3.6 or later\r\n')
    main()
