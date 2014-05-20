#!/usr/bin/env python
# wafw00f - Web Application Firewall Detection Tool
# by Sandro Gauci - enablesecurity.com (c) 2014
#  and Wendel G. Henrique - Trustwave 2009

__license__ = """
Copyright (c) 2014, {Sandro Gauci|Wendel G. Henrique}
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
try:
    import httplib
except ImportError:
    import http.client as httplib
try:
    from urllib import quote, unquote
except ImportError:
    from urllib.parse import quote, unquote
from optparse import OptionParser
import logging
import socket
import sys
import random

currentDir = os.getcwd()
scriptDir = os.path.dirname(sys.argv[0]) or '.'
os.chdir(scriptDir)

from wafw00f.lib.evillib import oururlparse, scrambledheader, waftoolsengine

__version__ = '0.9.2'

lackofart = """
                                 ^     ^
        _   __  _   ____ _   __  _    _   ____
       ///7/ /.' \ / __////7/ /,' \ ,' \ / __/
      | V V // o // _/ | V V // 0 // 0 // _/
      |_n_,'/_n_//_/   |_n_,' \_,' \_,'/_/
                                <
                                 ...'

    WAFW00F - Web Application Firewall Detection Tool

    By Sandro Gauci && Wendel G. Henrique
"""


class WafW00F(waftoolsengine):
    """
    WAF detection tool
    """

    AdminFolder = '/Admin_Files/'
    xssstring = '<script>alert(1)</script>'
    dirtravstring = '../../../../etc/passwd'
    cleanhtmlstring = '<invalid>hello'
    isaservermatch = [
                    'Forbidden ( The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.  )',
                    'Forbidden ( The ISA Server denied the specified Uniform Resource Locator (URL)']

    def __init__(self, target='www.microsoft.com', port=80, ssl=False,
                 debuglevel=0, path='/', followredirect=True):
        """
        target: the hostname or ip of the target server
        port: defaults to 80
        ssl: defaults to false
        """
        waftoolsengine.__init__(self, target, port, ssl, debuglevel, path, followredirect)
        self.log = logging.getLogger('wafw00f')
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
        string = self.path + self.cleanhtmlstring + '.html'
        return self.request(path=string, usecache=usecache, cacheresponse=cacheresponse)

    def xssstandard(self, usecache=True, cacheresponse=True):
        xssstringa = self.path + self.xssstring + '.html'
        return self.request(path=xssstringa, usecache=usecache, cacheresponse=cacheresponse)

    def protectedfolder(self, usecache=True, cacheresponse=True):
        pfstring = self.path + self.AdminFolder
        return self.request(path=pfstring, usecache=usecache, cacheresponse=cacheresponse)

    def xssstandardencoded(self, usecache=True, cacheresponse=True):
        xssstringa = self.path + quote(self.xssstring) + '.html'
        return self.request(path=xssstringa, usecache=usecache, cacheresponse=cacheresponse)

    def cmddotexe(self, usecache=True, cacheresponse=True):
        # thanks j0e
        string = self.path + 'cmd.exe'
        return self.request(path=string, usecache=usecache, cacheresponse=cacheresponse)

    attacks = [cmddotexe, directorytraversal, xssstandard, protectedfolder, xssstandardencoded]

    def genericdetect(self, usecache=True, cacheresponse=True):
        reason = ''
        reasons = ['Blocking is being done at connection/packet level.',
                   'The server header is different when an attack is detected.',
                   'The server returned a different response code when a string trigged the blacklist.',
                   'It closed the connection for a normal request.',
                   'The connection header was scrambled.'
                   ]
        # test if response for a path containing html tags with known evil strings
        # gives a different response from another containing invalid html tags
        r = self.cleanhtml()
        if r is None:
            self.knowledge['generic']['reason'] = reasons[0]
            self.knowledge['generic']['found'] = True
            return True
        cleanresponse, _tmp = r
        r = self.xssstandard()
        if r is None:
            self.knowledge['generic']['reason'] = reasons[0]
            self.knowledge['generic']['found'] = True
            return True
        xssresponse, _tmp = r
        if xssresponse.status != cleanresponse.status:
            self.log.info('Server returned a different response when a script tag was tried')
            reason = reasons[2]
            reason += '\r\n'
            reason += 'Normal response code is "%s",' % cleanresponse.status
            reason += ' while the response code to an attack is "%s"' % xssresponse.status
            self.knowledge['generic']['reason'] = reason
            self.knowledge['generic']['found'] = True
            return True
        r = self.cleanhtmlencoded()
        cleanresponse, _tmp = r
        r = self.xssstandardencoded()
        if r is None:
            self.knowledge['generic']['reason'] = reasons[0]
            self.knowledge['generic']['found'] = True
            return True
        xssresponse, _tmp = r
        if xssresponse.status != cleanresponse.status:
            self.log.info('Server returned a different response when a script tag was tried')
            reason = reasons[2]
            reason += '\r\n'
            reason += 'Normal response code is "%s",' % cleanresponse.status
            reason += ' while the response code to an attack is "%s"' % xssresponse.status
            self.knowledge['generic']['reason'] = reason
            self.knowledge['generic']['found'] = True
            return True
        response, responsebody = self.normalrequest()
        normalserver = response.getheader('Server')
        for attack in self.attacks:
            r = attack(self)
            if r is None:
                self.knowledge['generic']['reason'] = reasons[0]
                self.knowledge['generic']['found'] = True
                return True
            response, responsebody = r
            attackresponse_server = response.getheader('Server')
            if attackresponse_server:
                if attackresponse_server != normalserver:
                    self.log.info('Server header changed, WAF possibly detected')
                    self.log.debug('attack response: %s' % attackresponse_server)
                    self.log.debug('normal response: %s' % normalserver)
                    reason = reasons[1]
                    reason += '\r\nThe server header for a normal response is "%s",' % normalserver
                    reason += ' while the server header a response to an attack is "%s.",' % attackresponse_server
                    self.knowledge['generic']['reason'] = reason
                    self.knowledge['generic']['found'] = True
                    return True
        for attack in self.wafdetectionsprio:
            if self.wafdetections[attack](self) is None:
                self.knowledge['generic']['reason'] = reasons[0]
                self.knowledge['generic']['found'] = True
                return True
        for attack in self.attacks:
            r = attack(self)
            if r is None:
                self.knowledge['generic']['reason'] = reasons[0]
                self.knowledge['generic']['found'] = True
                return True
            response, responsebody = r
            for h, v in response.getheaders():
                if scrambledheader(h):
                    self.knowledge['generic']['reason'] = reasons[4]
                    self.knowledge['generic']['found'] = True
                    return True
        return False

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
            response, responsebody = r
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
                        if re.match(match, headerval, re.IGNORECASE):
                            detected = True
                            break
                    else:
                        if re.match(match, headerval):
                            detected = True
                            break
                if detected:
                    break
        return detected

    def isbigip(self):
        detected = False
        if self.matchheader(('X-Cnection', '^close$'), attack=True):
            return True
        # the following based on nmap's http-waf-fingerprint.nse
        elif self.matchheader(('server', 'BigIP')):
            return True
        # the following based on nmap's http-waf-fingerprint.nse
        elif self.matchcookie('^BIGipServer='):
            return True
        else:
            return False

    def iswebknight(self):
        detected = False
        for attack in self.attacks:
            r = attack(self)
            if r is None:
                return
            response, responsebody = r
            if response.status == 999:
                detected = True
                break
        return detected

    def ismodsecurity(self):
        detected = False
        for attack in self.attacks:
            r = attack(self)
            if r is None:
                return
            response, responsebody = r
            if response.status == 501:
                detected = True
                break
        # the following based on nmap's http-waf-fingerprint.nse
        if self.matchheader(('server', '(mod_security|Mod_Security|NOYB)')):
            return True
        return detected

    def isisaserver(self):
        detected = False
        r = self.invalidhost()
        if r is None:
            return
        response, responsebody = r
        if response.reason in self.isaservermatch:
            detected = True
        return detected

    def issecureiis(self):
        # credit goes to W3AF
        detected = False
        r = self.normalrequest()
        if r is None:
            return
        response, responsebody = r
        if response.status == 404:
            return
        headers = dict()
        headers['Transfer-Encoding'] = 'z' * 1025
        r = self.normalrequest(headers=headers)
        if r is None:
            return
        response, responsebody = r
        if response.status == 404:
            detected = True
        return detected

    def matchcookie(self, match):
        """
        a convenience function which calls matchheader
        """
        return self.matchheader(('set-cookie', match))

    def isairlock(self):
        # credit goes to W3AF
        return self.matchcookie('^AL[_-]?(SESS|LB)=')

    def isbarracuda(self):
        # credit goes to W3AF
        if self.matchcookie('^barra_counter_session='):
            return True
        # credit goes to Charlie Campbell
        if self.matchcookie('^BNI__BARRACUDA_LB_COOKIE='):
            return True
        return False

    def isdenyall(self):
        # credit goes to W3AF
        if self.matchcookie('^sessioncookie='):
            return True
        # credit goes to Sebastien Gioria
        #   Tested against a Rweb 3.8
        # and modified by sandro gauci and someone else
        for attack in self.attacks:
            r = attack(self)
            if r is None:
                return
            response, responsebody = r
            if response.status == 200:
                if response.reason == 'Condition Intercepted':
                    return True
        return False

    def isbeeware(self):
        # disabled cause it was giving way too many false positives
        # credit goes to Sebastien Gioria
        detected = False
        r = self.xssstandard()
        if r is None:
            return
        response, responsebody = r
        if (response.status != 200) or (response.reason == 'Forbidden'):
            r = self.directorytraversal()
            if r is None:
                return
            response, responsebody = r
            if response.status == 403:
                if response.reason == 'Forbidden':
                    detected = True
        return detected

    def isf5asm(self):
        # credit goes to W3AF
        return self.matchcookie('^TS[a-zA-Z0-9]{3,6}=')

    def isf5trafficshield(self):
        for hv in [['cookie', '^ASINFO='], ['server', 'F5-TrafficShield']]:
            r = self.matchheader(hv)
            if r is None:
                return
            elif r:
                return r
        # the following based on nmap's http-waf-fingerprint.nse
        if self.matchheader(('server', 'F5-TrafficShield')):
            return True
        return False

    def isteros(self):
        # credit goes to W3AF
        return self.matchcookie('^st8id=')

    def isnetcontinuum(self):
        # credit goes to W3AF
        return self.matchcookie('^NCI__SessionId=')

    def isbinarysec(self):
        # credit goes to W3AF
        if self.matchheader(('server', 'BinarySec')):
            return True
        # the following based on nmap's http-waf-fingerprint.nse
        elif self.matchheader(('x-binarysec-via', '.')):
            return True
        # the following based on nmap's http-waf-fingerprint.nse
        elif self.matchheader(('x-binarysec-nocache', '.')):
            return True
        else:
            return False

    def ishyperguard(self):
        # credit goes to W3AF
        return self.matchcookie('^WODSESSION=')

    def isprofense(self):
        """
        Checks for server headers containing "profense"
        """
        return self.matchheader(('server', 'profense'))

    def isnetscaler(self):
        """
        First checks if a cookie associated with Netscaler is present,
        if not it will try to find if a "Cneonction" or "nnCoection" is returned
        for any of the attacks sent
        """
        # NSC_ and citrix_ns_id come from David S. Langlands <dsl 'at' surfstar.com>
        if self.matchcookie('^(ns_af=|citrix_ns_id|NSC_)'):
            return True
        if self.matchheader(('Cneonction', 'close'), attack=True):
            return True
        if self.matchheader(('nnCoection', 'close'), attack=True):
            return True
        if self.matchheader(('Via', 'NS-CACHE'), attack=True):
            return True
        if self.matchheader(('x-client-ip', '.'), attack=True):
            return True
        return False

    def isurlscan(self):
        detected = False
        testheaders = dict()
        testheaders['Translate'] = 'z'*10
        testheaders['If'] = 'z'*10
        testheaders['Lock-Token'] = 'z'*10
        testheaders['Transfer-Encoding'] = 'z'*10
        r = self.normalrequest()
        if r is None:
            return
        response, _tmp = r
        r = self.normalrequest(headers=testheaders)
        if r is None:
            return
        response2, _tmp = r
        if response.status != response2.status:
            if response2.status == 404:
                detected = True
        return detected

    def iswebscurity(self):
        detected = False
        r = self.normalrequest()
        if r is None:
            return
        response, responsebody = r
        if response.status == 403:
            return detected
        newpath = self.path + '?nx=@@'
        r = self.request(path=newpath)
        if r is None:
            return
        response, responsebody = r
        if response.status == 403:
            detected = True
        return detected

    def isdotdefender(self):
        # thanks to j0e
        return self.matchheader(['X-dotDefender-denied', '^1$'], attack=True)

    def isimperva(self):
        # thanks to Mathieu Dessus <mathieu.dessus(a)verizonbusiness.com> for this
        # might lead to false positives so please report back to sandro@enablesecurity.com
        for attack in self.attacks:
            r = attack(self)
            if r is None:
                return
            response, responsebody = r
            if response.version == 10:
                return True
        return False

    def ismodsecuritypositive(self):
        detected = False
        self.normalrequest(usecache=False, cacheresponse=False)
        randomfn = self.path + str(random.randrange(1000, 9999)) + '.html'
        r = self.request(path=randomfn)
        if r is None:
            return
        response, responsebody = r
        if response.status != 302:
            return False
        randomfnnull = randomfn+'%00'
        r = self.request(path=randomfnnull)
        if r is None:
            return
        response, responsebody = r
        if response.status == 404:
            detected = True
        return detected

    def isincapsula(self):
        # credit goes to Charlie Campbell
        if self.matchcookie('^.incap_ses'):
            return True
        if self.matchcookie('^visid.*='):
            return True
        return False

    def isibmdatapower(self):
        # Added by Mathieu Dessus <mathieu.dessus(a)verizonbusiness.com>
        detected = False
        if self.matchheader(('X-Backside-Transport', '^(OK|FAIL)')):
            detected = True
        return detected


    def isibm(self):
        detected = False
        r = self.protectedfolder()
        if r is None:
            detected = True
        return detected

    # the following based on nmap's http-waf-fingerprint.nse
    def iscloudflare(self):
        if self.matchheader(('server', 'cloudflare-nginx')):
            return True
        if self.matchcookie('__cfduid'):
            return True
        return False

    def isuspses(self):
        if self.matchheader(('server', 'Secure Entry Server')):
            return True
        return False

    def isciscoacexml(self):
        if self.matchheader(('server', 'ACE XML Gateway')):
            return True
        return False

    wafdetections = dict()
    # easy ones
    wafdetections['IBM Web Application Security'] = isibm
    wafdetections['IBM DataPower'] = isibmdatapower
    wafdetections['Profense'] = isprofense
    wafdetections['ModSecurity'] = ismodsecurity
    wafdetections['ISA Server'] = isisaserver
    wafdetections['NetContinuum'] = isnetcontinuum
    wafdetections['HyperGuard'] = ishyperguard
    wafdetections['Barracuda'] = isbarracuda
    wafdetections['Airlock'] = isairlock
    wafdetections['BinarySec'] = isbinarysec
    wafdetections['F5 Trafficshield'] = isf5trafficshield
    wafdetections['F5 ASM'] = isf5asm
    wafdetections['Teros'] = isteros
    wafdetections['DenyALL'] = isdenyall
    wafdetections['BIG-IP'] = isbigip
    wafdetections['Citrix NetScaler'] = isnetscaler
    # lil bit more complex
    wafdetections['webApp.secure'] = iswebscurity
    wafdetections['WebKnight'] = iswebknight
    wafdetections['URLScan'] = isurlscan
    wafdetections['SecureIIS'] = issecureiis
    wafdetections['dotDefender'] = isdotdefender
    #wafdetections['BeeWare'] = isbeeware
    # wafdetections['ModSecurity (positive model)'] = ismodsecuritypositive removed for now
    wafdetections['Imperva'] = isimperva
    wafdetections['Incapsula'] = isincapsula
    wafdetections['Cloud Flare'] = iscloudflare
    wafdetections['Secure Entry Server'] = isuspses
    wafdetections['Cisco ACE XML Gateway'] = isciscoacexml
    wafdetectionsprio = ['Profense', 'NetContinuum', 'Incapsula', 'Cloud Flare',
                         'Secure Entry Server', 'Cisco ACE XML Gateway',
                         'Barracuda', 'HyperGuard', 'BinarySec', 'Teros',
                         'F5 Trafficshield', 'F5 ASM', 'Airlock', 'Citrix NetScaler',
                         'ModSecurity', 'IBM Web Application Security', 'IBM DataPower', 'DenyALL',
                         'dotDefender', 'webApp.secure',  # removed for now 'ModSecurity (positive model)',
                         'BIG-IP', 'URLScan', 'WebKnight',
                         'SecureIIS', 'Imperva', 'ISA Server']

    def identwaf(self, findall=False):
        detected = list()
        for wafvendor in self.wafdetectionsprio:
            self.log.info('Checking for %s' % wafvendor)
            if self.wafdetections[wafvendor](self):
                detected.append(wafvendor)
                if not findall:
                    break
        self.knowledge['wafname'] = detected
        return detected


def calclogginglevel(verbosity):
    default = 40 # errors are printed out
    level = default - (verbosity*10)
    if level < 0:
        level = 0
    return level


class wafwoof_api:
    def __init__(self):
        self.cache = dict()

    def vendordetect(self, url, findall=False):
        if self.cache.has_key(url):
            wafw00f = self.cache[url]
        else:
            r = oururlparse(url)
            if r is None:
                return ['']
            (hostname, port, path, query, ssl) = r
            wafw00f = WafW00F(target=hostname, port=port, path=path, ssl=ssl)
            self.cache[url] = wafw00f
        return wafw00f.identwaf(findall=findall)

    def genericdetect(self, url):
        if self.cache.has_key(url):
            wafw00f = self.cache[url]
        else:
            r = oururlparse(url)
            if r is None:
                return {}
            (hostname, port, path, query, ssl) = r
            wafw00f = WafW00F(target=hostname, port=port, path=path, ssl=ssl)
            self.cache[url] = wafw00f
        wafw00f.genericdetect()
        return wafw00f.knowledge['generic']

    def alltests(self, url, findall=False):
        if self.cache.has_key(url):
            wafw00f = self.cache[url]
        else:
            r = oururlparse(url)
            if r is None:
                return {}
            (hostname, port, path, query, ssl) = r
            wafw00f = WafW00F(target=hostname, port=port, path=path, ssl=ssl)
            self.cache[url] = wafw00f
        wafw00f.identwaf(findall=findall)
        if (len(wafw00f.knowledge['wafname']) == 0) or (findall):
            wafw00f.genericdetect()
        return wafw00f.knowledge


def xmlrpc_interface(bindaddr=('localhost', 8001)):
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)

    server = SimpleXMLRPCServer(bindaddr,
                                requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_instance(wafwoof_api())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('bye!')
        return


def main():
    print(lackofart)
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
    parser.add_option('--xmlrpc', dest='xmlrpc', action='store_true',
                      default=False, help='Switch on the XML-RPC interface instead of CUI')
    parser.add_option('--xmlrpcport', dest='xmlrpcport', type='int',
                      default=8001, help='Specify an alternative port to listen on, default 8001')
    parser.add_option('--version', '-V', dest='version', action='store_true',
                      default=False, help='Print out the version')
    options, args = parser.parse_args()
    logging.basicConfig(level=calclogginglevel(options.verbose))
    log = logging.getLogger()
    if options.list:
        print('Can test for these WAFs:\r\n')
        attacker = WafW00F(None)
        print('\r\n'.join(attacker.wafdetectionsprio))
        return
    if options.version:
        print('WAFW00F version %s' % __version__)
        return
    elif options.xmlrpc:
        print('Starting XML-RPC interface')
        xmlrpc_interface(bindaddr=('localhost', options.xmlrpcport))
        return
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
        (hostname, port, path, query, ssl) = pret
        log.info('starting wafw00f on %s' % target)
        attacker = WafW00F(hostname, port=port, ssl=ssl,
                           debuglevel=options.verbose, path=path,
                           followredirect=options.followredirect)
        if attacker.normalrequest() is None:
            log.error('Site %s appears to be down' % target)
            sys.exit(1)
        if options.test:
            if attacker.wafdetections.has_key(options.test):
                waf = attacker.wafdetections[options.test](attacker)
                if waf:
                    print('The site %s is behind a %s' % (target, options.test))
                else:
                    print('WAF %s was not detected on %s' % (options.test, target))
            else:
                print('WAF %s was not found in our list\r\nUse the --list option to see what is available' % options.test)
            return
        waf = attacker.identwaf(options.findall)
        log.info('Ident WAF: %s' % waf)
        if len(waf) > 0:
            print('The site %s is behind a %s' % (target, ' and/or '.join(waf)))
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
    if sys.hexversion < 0x2040000:
        sys.stderr.write('Your version of python is way too old .. please update to 2.4 or later\r\n')
    main()
