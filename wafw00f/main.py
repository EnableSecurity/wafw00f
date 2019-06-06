#!/usr/bin/env python
# wafw00f - Web Application Firewall Detection Tool
# by Sandro Gauci - enablesecurity.com (c) 2016
#  and Wendel G. Henrique - Trustwave 2009

__license__ = """
Copyright (c) 2016, {Sandro Gauci|Wendel G. Henrique}
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of EnableSecurity or Trustwave nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
import logging
import sys, re
import random, io
try:
    import httplib
except ImportError:
    import http.client as httplib
try:
    from urllib import quote, unquote
except ImportError:
    from urllib.parse import quote, unquote
from optparse import OptionParser

# Colors for terminal
W = '\033[1;97m'
Y = '\033[1;93m'
G = '\033[1;92m'
R = '\033[1;91m'
B = '\033[1;94m'
C = '\033[1;96m'
E = '\033[0m'

# Windows based systems do not support ANSI sequences,
# hence not displaying them.
if 'win' in sys.platform:
    W = Y = G = R = B = C = E = ''

currentDir = os.getcwd()
scriptDir = os.path.dirname(sys.argv[0]) or '.'
os.chdir(scriptDir)

from wafw00f import __version__
from wafw00f.lib.evillib import oururlparse, scrambledheader, waftoolsengine
from wafw00f.manager import load_plugins
from wafw00f.wafprio import wafdetectionsprio

# Phew! WAF says a Woof! You know who's the good boy. :)
woof = '''
                 '''+W+'''______
                '''+W+'''/      \\
               '''+W+'''(  Woof! )
                '''+W+'''\______/                      '''+R+''')
                '''+W+''',,                           '''+R+''') ('''+Y+'''_
           '''+Y+'''.-. '''+W+'''-    '''+G+'''_______                 '''+R+'''( '''+Y+'''|__|
          '''+Y+'''()``; '''+G+'''|==|_______)                '''+R+'''.)'''+Y+'''|__|
          '''+Y+'''/ ('        '''+G+'''/|\                  '''+R+'''(  '''+Y+'''|__|
      '''+Y+'''(  /  )       '''+G+''' / | \                  '''+R+'''. '''+Y+'''|__|
       '''+Y+'''\(_)_))      '''+G+'''/  |  \                   '''+Y+'''|__|'''+E+'''

    WAFW00F - Web Application Firewall Detection Tool
    '''

class WafW00F(waftoolsengine):

    AdminFolder = '/Admin_Files/'
    xssstring = '<script>alert(1)</script>'
    dirtravstring = '../../../../etc/passwd'
    cleanhtmlstring = '<invalid>hello'

    def __init__(self, target='www.example.com', port=80, ssl=False,
                 debuglevel=0, path='/', followredirect=True, extraheaders={}, proxy=False):
        """
        target: the hostname or ip of the target server
        port: defaults to 80
        ssl: defaults to false
        """
        self.log = logging.getLogger('wafw00f')
        waftoolsengine.__init__(self, target, port, ssl, debuglevel, path, followredirect, extraheaders, proxy)
        self.knowledge = dict(generic=dict(found=False, reason=''), wafname=list())

    def normalrequest(self, usecache=True, cacheresponse=True, headers=None):
        return self.request(usecache=usecache, cacheresponse=cacheresponse, headers=headers)

    def normalnonexistentfile(self, usecache=True, cacheresponse=True):
        path = self.path + str(random.randrange(1000, 9999)) + '.html'
        return self.request(path=path, usecache=usecache, cacheresponse=cacheresponse)

    def unknownmethod(self, usecache=True, cacheresponse=True):
        return self.request(method='OHYEA', usecache=usecache, cacheresponse=cacheresponse)

    def directorytraversal(self, usecache=True, cacheresponse=True):
        return self.request(path=self.path + self.dirtravstring, usecache=usecache, cacheresponse=cacheresponse)

    def invalidhost(self, usecache=True, cacheresponse=True):
        randomnumber = random.randrange(100000, 999999)
        return self.request(headers={'Host': str(randomnumber)})

    def cleanhtmlencoded(self, usecache=True, cacheresponse=True):
        string = self.path + quote(self.cleanhtmlstring) + '.html'
        return self.request(path=string, usecache=usecache, cacheresponse=cacheresponse)

    def cleanhtml(self, usecache=True, cacheresponse=True):
        string = self.path + '?htmli=' + self.cleanhtmlstring
        return self.request(path=string, usecache=usecache, cacheresponse=cacheresponse)

    def xssstandard(self, usecache=True, cacheresponse=True):
        xssstringa = self.path + '?xss=' + self.xssstring
        return self.request(path=xssstringa, usecache=usecache, cacheresponse=cacheresponse)

    def protectedfolder(self, usecache=True, cacheresponse=True):
        pfstring = self.path + self.AdminFolder
        return self.request(path=pfstring, usecache=usecache, cacheresponse=cacheresponse)

    def xssstandardencoded(self, usecache=True, cacheresponse=True):
        xssstringb = self.path + quote(self.xssstring) + '.html'
        return self.request(path=xssstringb, usecache=usecache, cacheresponse=cacheresponse)

    attacks = [xssstandard, directorytraversal, protectedfolder, xssstandardencoded]

    def genericdetect(self, usecache=True, cacheresponse=True):
        knownflops = [
            ('Microsoft-IIS/7.0','Microsoft-HTTPAPI/2.0'),
        ]
        reason = ''
        reasons = ['Blocking is being done at connection/packet level.',
                   'The server header is different when an attack is detected.',
                   'The server returned a different response code when a string trigged the blacklist.',
                   'It closed the connection for a normal request.',
                   'The connection header was scrambled.'
        ]
        # test if response for a path containing html tags with known evil strings
        # gives a different response from another containing invalid html tags
        try:
            cleanresponse, _tmp = self._perform_and_check(self.cleanhtml)
            xssresponse, _tmp = self._perform_and_check(self.xssstandard)
            if xssresponse.status != cleanresponse.status:
                self.log.info('Server returned a different response when a script tag was tried')
                reason = reasons[2]
                reason += '\r\n'
                reason += 'Normal response code is "%s",' % cleanresponse.status
                reason += ' while the response code to an attack is "%s"' % xssresponse.status
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return True
            cleanresponse, _tmp = self._perform_and_check(self.cleanhtmlencoded)
            xssresponse, _tmp = self._perform_and_check(self.xssstandardencoded)
            if xssresponse.status != cleanresponse.status:
                self.log.info('Server returned a different response when a script tag was tried')
                reason = reasons[2]
                reason += '\r\n'
                reason += 'Normal response code is "%s",' % cleanresponse.status
                reason += ' while the response code to an attack is "%s"' % xssresponse.status
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return True
            response, _ = self._perform_and_check(self.normalrequest)
            normalserver = response.getheader('Server')
            for attack in self.attacks:
                response, _ = self._perform_and_check(lambda: attack(self))
                attackresponse_server = response.getheader('Server')
                if attackresponse_server:
                    if attackresponse_server != normalserver:
                        if (normalserver, attackresponse_server) in knownflops:
                            return False
                        self.log.info('Server header changed, WAF possibly detected')
                        self.log.debug('attack response: %s' % attackresponse_server)
                        self.log.debug('normal response: %s' % normalserver)
                        reason = reasons[1]
                        reason += '\r\nThe server header for a normal response is "%s",' % normalserver
                        reason += ' while the server header a response to an attack is "%s",' % attackresponse_server
                        self.knowledge['generic']['reason'] = reason
                        self.knowledge['generic']['found'] = True
                        return True
            for attack in wafdetectionsprio:
                if self.wafdetections[attack](self) is None:
                    self.knowledge['generic']['reason'] = reasons[0]
                    self.knowledge['generic']['found'] = True
                    return True
            for attack in self.attacks:
                response, _ = self._perform_and_check(lambda: attack(self))
                for h, _ in response.getheaders():
                    if scrambledheader(h):
                        self.knowledge['generic']['reason'] = reasons[4]
                        self.knowledge['generic']['found'] = True
                        return True
        except RequestBlocked:
            self.knowledge['generic']['reason'] = reasons[0]
            self.knowledge['generic']['found'] = True
            return True

        return False

    def _perform_and_check(self, request_method):
        r = request_method()
        if r is None:
            raise RequestBlocked()

        return r

    def matchheader(self, headermatch, attack=False, ignorecase=True):
        import re

        detected = False
        header, match = headermatch
        if attack:
            requests = self.attacks
        else:
            requests = [self.normalrequest]
        for request in requests:
            r = request(self)
            if r is None:
                return
            response, _ = r
            headerval = response.getheader(header)
            if headerval:
                # set-cookie can have multiple headers, python gives it to us
                # concatinated with a comma
                if header == 'set-cookie':
                    headervals = headerval.split(', ')
                else:
                    headervals = [headerval]
                for headerval in headervals:
                    if ignorecase:
                        if re.search(match, headerval, re.IGNORECASE):
                            detected = True
                            break
                    else:
                        if re.search(match, headerval):
                            detected = True
                            break
                if detected:
                    break
        return detected

    def matchcookie(self, match):
        """
        a convenience function which calls matchheader
        """
        return self.matchheader(('set-cookie', match))

    wafdetections = dict()

    plugin_dict = load_plugins()
    result_dict = {}
    for plugin_module in plugin_dict.values():
        wafdetections[plugin_module.NAME] = plugin_module.is_waf

    def identwaf(self, findall=False):
        detected = list()

        # Check for prioritized ones first, then check those added externally
        checklist = wafdetectionsprio
        checklist += list(set(self.wafdetections.keys()) - set(checklist))

        for wafvendor in checklist:
            self.log.info('Checking for %s' % wafvendor)
            if self.wafdetections[wafvendor](self):
                detected.append(wafvendor)
                if not findall:
                    break
        self.knowledge['wafname'] = detected
        return detected


def calclogginglevel(verbosity):
    default = 40  # errors are printed out
    level = default - (verbosity * 10)
    if level < 0:
        level = 0
    return level


def getheaders(fn):
    headers = {}
    fullfn = os.path.abspath(os.path.join(os.getcwd(), fn))
    if not os.path.exists(fullfn):
        logging.getLogger('wafw00f').critical('Headers file "%s" does not exist!' % fullfn)
        return
    with io.open(fn, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            _t = line.split(':', 2)
            if len(_t) == 2:
                h, v = map(lambda x: x.strip(), _t)
                headers[h] = v
    return headers


def main():
    print(woof)
    parser = OptionParser(usage='%prog url1 [url2 [url3 ... ]]\r\nexample: %prog http://www.victim.org/')
    parser.add_option('-v', '--verbose', action='count', dest='verbose', default=0,
                      help='enable verbosity - multiple -v options increase verbosity')
    parser.add_option('-a', '--findall', action='store_true', dest='findall', default=False,
                      help='Find all WAFs, do not stop testing on the first one')
    parser.add_option('-r', '--disableredirect', action='store_false', dest='followredirect',
                      default=True, help='Do not follow redirections given by 3xx responses')
    parser.add_option('-t', '--test', dest='test',
                      help='Test for one specific WAF')
    parser.add_option('-l', '--list', dest='list', action='store_true',
                      default=False, help='List all WAFs that we are able to detect')
    parser.add_option('-p', '--proxy', dest='proxy',
                      default=False, help='Use an HTTP proxy to perform requests, example: http://hostname:8080, socks5://hostname:1080')
    parser.add_option('--version', '-V', dest='version', action='store_true',
                      default=False, help='Print out the version')
    parser.add_option('--headersfile', '-H', dest='headersfile', 
                      action='store', default=None, 
                      help='Pass custom headers, for example to overwrite the default User-Agent string')
    options, args = parser.parse_args()
    logging.basicConfig(level=calclogginglevel(options.verbose))
    log = logging.getLogger()
    if options.list:
        print('Can test for these WAFs:\r\n')
        attacker = WafW00F(None)
        print('\r\n'.join(attacker.wafdetections.keys()))
        return
    if options.version:
        print('WAFW00F version %s' % __version__)
        return
    extraheaders = {}
    if options.headersfile:
        log.info('Getting extra headers from %s' % options.headersfile)
        extraheaders = getheaders(options.headersfile)
        if extraheaders is None:
            parser.error('Please provide a headers file with colon delimited header names and values')
    if len(args) == 0:
        parser.error('we need a target site')
    targets = args
    for target in targets:
        if not (target.startswith('http://') or target.startswith('https://')):
            log.info('The url %s should start with http:// or https:// .. fixing (might make this unusable)' % target)
            target = 'http://' + target
        print('Checking %s' % target)
        pret = oururlparse(target)
        if pret is None:
            log.critical('The url %s is not well formed' % target)
            sys.exit(1)
        (hostname, port, path, _, ssl) = pret
        log.info('starting wafw00f on %s' % target)
        attacker = WafW00F(hostname, port=port, ssl=ssl,
                           debuglevel=options.verbose, path=path,
                           followredirect=options.followredirect,
                           extraheaders=extraheaders,
                           proxy=options.proxy)
        if attacker.normalrequest() is None:
            log.error('Site %s appears to be down' % target)
            continue
        if options.test:
            if options.test in attacker.wafdetections:
                waf = attacker.wafdetections[options.test](attacker)
                if waf:
                    print('The site %s is behind %s WAF.' % (target, options.test))
                else:
                    print('WAF %s was not detected on %s' % (options.test, target))
            else:
                print(
                    'WAF %s was not found in our list\r\nUse the --list option to see what is available' % options.test)
            return
        waf = attacker.identwaf(options.findall)
        log.info('Ident WAF: %s' % waf)
        if len(waf) > 0:
            print('The site %s is behind %s WAF.' % (target, ' and/or '.join(waf)))
        if (options.findall) or len(waf) == 0:
            print('Generic Detection results:')
            if attacker.genericdetect():
                log.info('Generic Detection: %s' % attacker.knowledge['generic']['reason'])
                print('The site %s seems to be behind a WAF or some sort of security solution' % target)
                print('Reason: %s' % attacker.knowledge['generic']['reason'])
            else:
                print('No WAF detected by the generic detection')
        print('Number of requests: %s' % attacker.requestnumber)


class RequestBlocked(Exception):
    pass


if __name__ == '__main__':
    if sys.hexversion < 0x2060000:
        sys.stderr.write('Your version of python is way too old .. please update to 2.6 or later\r\n')
    main()
