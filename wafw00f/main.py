#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

import logging
import os, io
import random
import sys, re
from optparse import OptionParser

from wafw00f import __version__
from wafw00f.manager import load_plugins
from wafw00f.wafprio import wafdetectionsprio
from wafw00f.lib.evillib import urlParser, waftoolsengine, scrambledHeader

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

# WOOF! Yes you heard it! WAF says a Woof! You know who's the good boy. ;)
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

    WAFW00F - Web Application Firewall Detection Tool (v1.0)
    '''

class WAFW00F(waftoolsengine):

    xsstring = '<script>alert("XSS");</script>'
    sqlistring = "UNION SELECT ALL FROM information_schema"
    lfistring = '../../../../etc/passwd'
    rcestring = '/bin/cat /etc/passwd; ping 127.0.0.1; curl google.com'
    xxestring = '<!ENTITY xxe SYSTEM "file:///etc/shadow" >]><pwn>&hack;</pwn>'

    def __init__(self, target='www.example.com', port=None, debuglevel=0, path='/',
                 followredirect=True, extraheaders={}, proxy=None, auth=None):
        
        self.log = logging.getLogger('wafw00f')
        self.attackres = None
        waftoolsengine.__init__(self, target, port, debuglevel, path, proxy, followredirect, auth, extraheaders)
        self.knowledge = dict(generic=dict(found=False, reason=''), wafname=list())

    def normalRequest(self, headers=None):
        return self.Request()

    def nonExistent(self):
        return self.Request(path=self.path + str(random.randrange(100, 999)) + '.html')

    def xssAttack(self):
        return self.Request(path=self.path, params= {'s': self.xsstring})

    def xxeAttack(self):
        return self.Request(path=self.path, params= {'s': self.xxestring})

    def lfiAttack(self):
        return self.Request(path=self.path + self.lfistring)

    def centralAttack(self):
        return self.Request(path=self.path, params= {'a': self.xsstring, 'b': self.sqlistring})

    def sqliAttack(self):
        return self.Request(path=self.path, params= {'s': self.sqlistring})

    def oscAttack(self):
        return self.Request(path=self.path, params= {'s': self.rcestring})

    def performCheck(self, request_method):
        r = request_method()
        if r is None:
            raise RequestBlocked()
        return r

    # Most common attacks used to detect WAFs
    attcom = [xssAttack, sqliAttack]
    attacks = [xssAttack, xxeAttack, lfiAttack, sqliAttack, oscAttack]

    def genericdetect(self):
        reason = ''
        reasons = ['Blocking is being done at connection/packet level.',
                   'The server header is different when an attack is detected.',
                   'The server returns a different response code when an attack string is used.',
                   'It closed the connection for a normal request.',
                   'The connection header was scrambled.'
                ]
        try:
            # Testing the status code upon sending a malicious request
            resp1 = self.performCheck(self.normalRequest)
            resp2 = self.performCheck(self.xssAttack)
            if resp1.status_code != resp2.status_code:
                self.log.info('Server returned a different response when a script tag was tried')
                reason = reasons[2]
                reason += '\r\n'
                reason += 'Normal response code is "%s",' % resp1.status_code
                reason += ' while the response code to an attack is "%s"' % resp2.status_code
                self.knowledge['generic']['reason'] = reason
                self.knowledge['generic']['found'] = True
                return True
            # Checking for the Server header after sending malicious requests
            response = self.performCheck(self.normalRequest)
            normalserver = response.headers.get('Server')
            for attack in self.attacks:
                response = self.performCheck(lambda: attack(self))
                attackresponse_server = response.headers.get('Server')
                if attackresponse_server:
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
            # When we're blank on what happened :(
            for attack in wafdetectionsprio:
                if not self.wafdetections[attack](self):
                    self.knowledge['generic']['reason'] = reasons[0]
                    self.knowledge['generic']['found'] = True
                    return True
            # When the headers are scrambled, we've a clue
            for attack in self.attacks:
                response = self.performCheck(lambda: attack(self))
                for h, _ in response.headers():
                    if scrambledHeader(h):
                        self.knowledge['generic']['reason'] = reasons[4]
                        self.knowledge['generic']['found'] = True
                        return True
        # If at all request doesn't go, press F
        except RequestBlocked:
            self.knowledge['generic']['reason'] = reasons[0]
            self.knowledge['generic']['found'] = True
            return True
        return False

    def matchHeader(self, headermatch, attack=False):
        r = self.attackres
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
        r = self.attackres
        if r is None:
            return
        if r.status_code == statuscode:
            return True
        return False

    def matchCookie(self, match, attack=False):
        return self.matchHeader(('Set-Cookie', match), attack=attack)

    def matchReason(self, reasoncode, attack=True):
        r = self.attackres
        if r is None:
            return
        # We may need to match multiline context in response body
        if str(r.reason) == reasoncode:
            return True
        return False

    def matchContent(self, regex, attack=True):
        r = self.attackres
        if r is None:
            return
        # We may need to match multiline context in response body
        if re.search(regex, r.text, re.I|re.M):
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
        self.attackres = self.performCheck(self.centralAttack)
        for wafvendor in self.checklist:
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

class RequestBlocked(Exception):
    pass

def main():
    print(woof)
    parser = OptionParser(usage='%prog url1 [url2 [url3 ... ]]\r\nexample: %prog http://www.victim.org/')
    parser.add_option('-v', '--verbose', action='count', dest='verbose', default=0,
                      help='Enable verbosity, multiple -v options increase verbosity')
    parser.add_option('-a', '--findall', action='store_true', dest='findall', default=False,
                      help='Find all WAFs which match the signatures, do not stop testing on the first one')
    parser.add_option('-r', '--noredirect', action='store_false', dest='followredirect',
                      default=True, help='Do not follow redirections given by 3xx responses')
    parser.add_option('-t', '--test', dest='test', help='Test for one specific WAF')
    parser.add_option('-l', '--list', dest='list', action='store_true',
                      default=False, help='List all WAFs that WAFW00F is able to detect')
    parser.add_option('-p', '--proxy', dest='proxy', default=None, 
                      help='Use an HTTP proxy to perform requests, example: http://hostname:8080, socks5://hostname:1080')
    parser.add_option('--auth', dest='auth', default=None, help='Use custom authentication for the proxy supplied in                     the format user:pass')
    parser.add_option('--version', '-V', dest='version', action='store_true',
                      default=False, help='Print out the current version of WafW00f and exit.')
    parser.add_option('--headers', '-H', dest='headers', action='store', default=None, 
                      help='Pass custom headers via a text file to overwrite the default header set.')
    options, args = parser.parse_args()
    logging.basicConfig(level=calclogginglevel(options.verbose))
    log = logging.getLogger()
    if options.list:
        print('Can test for these WAFs:\r\n')
        attacker = WAFW00F(None)
        print('\r\n'.join(attacker.wafdetections.keys()))
        return
    if options.version:
        print('WAFW00F Version %s' % __version__)
        return
    extraheaders = {}
    if options.headers:
        log.info('Getting extra headers from %s' % options.headers)
        extraheaders = getheaders(options.headers)
        if extraheaders is None:
            parser.error('Please provide a headers file with colon delimited header names and values')
    if len(args) == 0:
        parser.error('No test target specified.')
    targets = args
    for target in targets:
        if not target.startswith('http'):
            log.info('The url %s should start with http:// or https:// .. fixing (might make this unusable)' % target)
            target = 'http://' + target
        print('Checking %s' % target)
        pret = urlParser(target)
        if pret is None:
            log.critical('The url %s is not well formed' % target)
            sys.exit(1)
        (hostname, port, path, _, _) = pret
        log.info('starting wafw00f on %s' % target)
        attacker = WAFW00F(target, port=port, debuglevel=options.verbose, path=path,
                    followredirect=options.followredirect, extraheaders=extraheaders,
                        proxy=options.proxy, auth=options.auth)
        if attacker.normalRequest() is None:
            log.error('Site %s appears to be down' % hostname)
            continue
        if options.test:
            if options.test in attacker.wafdetections:
                waf = attacker.wafdetections[options.test](attacker)
                if waf:
                    print('The site %s is behind %s WAF.' % (target, options.test))
                else:
                    print('WAF %s was not detected on %s' % (options.test, target))
            else:
                print('WAF %s was not found in our list\r\nUse the --list option to see what is available' % options.test)
            return
        waf = attacker.identwaf(options.findall)
        log.info('Identified WAF: %s' % waf)
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

if __name__ == '__main__':
    if sys.hexversion < 0x2060000:
        sys.stderr.write('Your version of python is way too old .. please update to 2.6 or later\r\n')
    main()
