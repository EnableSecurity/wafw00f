#!/usr/bin/env python
import re
import sys

import socket

try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse
import logging

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.stderr.write('You need to get BeautifulSoup installed\n')
    sys.stderr.write('Do it now, as privileged user/root run: pip install beautifulsoup4\now')
    sys.exit(1)


from .proxy import NullProxy, HttpProxy, Socks5Proxy, httplib, socks

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



# unicode mapping borrowed from http://packetstormsecurity.org/web/unicode-fun.txt
# by Gary O'leary-Steele of Sec-1 Ltd
try:
    from urllib import quote, unquote
except ImportError:
    from urllib.parse import quote, unquote
unicodemapping = {' ': '%u0020',
                  '/': '%u2215',
                  '\\': '%u2215',
                  "'": '%u02b9',
                  '"': '%u0022',
                  '>': '%u003e',
                  '<': '%u003c',
                  '#': '%uff03',
                  '!': '%uff01',
                  '$': '%uff04',
                  '*': '%uff0a',
                  '@': '%u0040',
                  '.': '%uff0e',
                  '_': '%uff3f',
                  '(': '%uff08',
                  ')': '%uff09',
                  ',': '%uff0c',
                  '%': '%u0025',
                  '-': '%uff0d',
                  ';': '%uff1b',
                  ':': '%uff1a',
                  '|': '%uff5c',
                  '&': '%uff06',
                  '+': '%uff0b',
                  '=': '%uff1d',
                  'a': '%uff41',
                  'A': '%uff21',
                  'b': '%uff42',
                  'B': '%uff22',
                  'c': '%uff43',
                  'C': '%uff23',
                  'd': '%uff44',
                  'D': '%uff24',
                  'e': '%uff45',
                  'E': '%uff25',
                  'f': '%uff46',
                  'F': '%uff26',
                  'g': '%uff47',
                  'G': '%uff27',
                  'h': '%uff48',
                  'H': '%uff28',
                  'i': '%uff49',
                  'I': '%uff29',
                  'j': '%uff4a',
                  'J': '%uff2a',
                  'k': '%uff4b',
                  'K': '%uff2b',
                  'l': '%uff4c',
                  'L': '%uff2c',
                  'm': '%uff4d',
                  'M': '%uff2d',
                  'n': '%uff4e',
                  'N': '%uff2e',
                  'o': '%uff4f',
                  'O': '%uff2f',
                  'p': '%uff50',
                  'P': '%uff30',
                  'q': '%uff51',
                  'Q': '%uff31',
                  'r': '%uff52',
                  'R': '%uff32',
                  's': '%uff53',
                  'S': '%uff33',
                  't': '%uff54',
                  'T': '%uff34',
                  'u': '%uff55',
                  'U': '%uff35',
                  'v': '%uff56',
                  'V': '%uff36',
                  'w': '%uff57',
                  'W': '%uff37',
                  'x': '%uff58',
                  'X': '%uff38',
                  'y': '%uff59',
                  'Y': '%uff39',
                  'z': '%uff5a',
                  'Z': '%uff3a',
                  '0': '%uff10',
                  '1': '%uff11',
                  '2': '%uff12',
                  '3': '%uff13',
                  '4': '%uff14',
                  '5': '%uff15',
                  '6': '%uff16',
                  '7': '%uff17',
                  '8': '%uff18',
                  '9': '%uff19'}

homoglyphicmapping = {"'": '%ca%bc'}


def oururlparse(target):
    log = logging.getLogger('urlparser')

    ssl = False
    o = urlparse(target)
    if o[0] not in ['http', 'https', '']:
        log.error('scheme %s not supported' % o[0])
        return
    if o[0] == 'https':
        ssl = True
    if len(o[2]) > 0:
        path = o[2]
    else:
        path = '/'
    tmp = o[1].split(':')
    if len(tmp) > 1:
        port = tmp[1]
    else:
        port = None
    hostname = tmp[0]
    query = o[4]
    return (hostname, port, path, query, ssl)


def modifyurl(path, modfunc, log):
    path = path
    log.debug('path is currently %s' % path)
    #s = re.search('(\[.*?\])',path)
    for m in re.findall('(\[.*?\])', path):
        ourstr = m[1:-1]
        newstr = modfunc(ourstr)
        log.debug('String was %s' % ourstr)
        log.debug('String became %s' % newstr)
        path = path.replace(m, newstr)
    log.debug('the path is now %s' % path)
    return path


def modifypath(path, newstrs, log, encode=True):
    log.debug('path is currently %s' % path)
    for m in re.findall('(\[.*?\])', path):
        ourstr = m[1:-1]
        for newstr in newstrs:
            if encode:
                newstr = quote(newstr)
            log.debug('String was %s' % ourstr)
            log.debug('String became %s' % newstr)
            newpath = path.replace(m, newstr).replace(']', '').replace('[', '')
            yield (newpath)


def bruteforceascii(ourstr):
    listourstr = list(ourstr)
    for pos in range(len(ourstr)):
        for i in range(256):
            newlistourstr = listourstr[:]
            newlistourstr[pos] = chr(i)
            yield (quote(''.join(newlistourstr)))


def unicodeurlencode(ourstr):
    newstr = str()
    for character in ourstr:
        if unicodemapping.has_key(character):
            newstr += unicodemapping[character]
        else:
            newstr += character
    return newstr


def nullify(ourstr):
    newstr = str()
    for character in ourstr:
        newstr += character + "\x00"
    return quote(newstr)


def replacechars(ourstr, origchar, newchar):
    newstr = ourstr.replace(origchar, newchar)
    return newstr


def nullifyspaces(ourstr):
    return quote(replacechars(ourstr, ' ', '\x00'))


def slashspaces(ourstr):
    return replacechars(ourstr, ' ', '/')


def tabifyspaces(ourstr):
    return replacechars(ourstr, ' ', '\t')


def crlfspaces(ourstr):
    return replacechars(ourstr, ' ', '\n')


def backslashquotes(ourstr):
    return replacechars(ourstr, "'", "\''")


class waftoolsengine:
    def __init__(self, target='www.microsoft.com', port=80, ssl=False,
                 debuglevel=0, path='/', followredirect=True, extraheaders={},
                 proxy=False):
        """
        target: the hostname or ip of the target server
        port: defaults to 80
        ssl: defaults to false
        """
        self.target = target
        if port is None:
            if ssl:
                port = 443
            else:
                port = 80
        self.port = int(port)
        self.ssl = ssl
        self.debuglevel = debuglevel
        self.cachedresponses = dict()
        self.requestnumber = 0
        self.path = path
        self.redirectno = 0
        self.followredirect = followredirect
        self.crawlpaths = list()
        self.extraheaders = extraheaders

        try:
            self.proxy = self._parse_proxy(proxy) if proxy else NullProxy()
        except Exception as e:
            self.log.critical("Proxy disabled: %s" % e)
            self.proxy = NullProxy()

    def request(self, method='GET', path=None, usecache=True,
                cacheresponse=True, headers=None,
                comingfromredir=False):
        followredirect = self.followredirect
        if comingfromredir:
            self.redirectno += 1
            if self.redirectno >= 5:
                self.log.error('We received way too many redirects.. stopping that')
                followredirect = False
        else:
            self.redirectno = 0
        if path is None:
            path = self.path
        for hdr in self.extraheaders.keys():
            if headers is None:
                headers = {}
            headers[hdr] = self.extraheaders[hdr]
        if headers is not None:
            knownheaders = map(lambda x: x.lower(), headers.keys())
        else:
            knownheaders = {}
            headers = {}
        if not 'user-agent' in knownheaders:
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b1) Gecko/20081007 Firefox/3.0'
        if not 'accept-charset' in knownheaders:
            headers['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
        if not 'accept' in knownheaders:
            headers['Accept'] = '*/*'
        k = str([method, path, headers])
        if usecache:
            if k in self.cachedresponses.keys():
                self.log.debug('Using cached version of %s, %s' % (method, path))
                return self.cachedresponses[k]
            else:
                self.log.debug('%s not found in %s' % (k, self.cachedresponses.keys()))
        r = self._request(method, path, headers)
        if cacheresponse:
            self.cachedresponses[k] = r

        if r:
            response, responsebody = r
            if response.status in [301, 302, 307]:
                if followredirect:
                    if response.getheader('location'):
                        newloc = response.getheader('location')
                        self.log.info('Redirected to %s' % newloc)
                        pret = oururlparse(newloc)
                        if pret is not None:
                            (target, port, path, query, ssl) = pret
                            if not port: port = 80
                            if target == '':
                                target = self.target
                            if port is None:
                                port = self.port
                            if not path.startswith('/'):
                                path = '/' + path
                            if (target, port, ssl) == (self.target, self.port, ssl):
                                r = self.request(method, path, usecache, cacheresponse,
                                                 headers, comingfromredir=True)
                            else:
                                self.log.warn('Tried to redirect to a different server %s' % newloc)
                        else:
                            self.log.warn('%s is not a well formatted url' % response.getheader('location'))
        return r

    def _request(self, method, path, headers):
        original_socket = socket.socket
        try:
            conn_factory, connect_host, connect_port, query_path = \
                    self.proxy.prepare(self.target, self.port, path, self.ssl)

            params = dict()
            if sys.hexversion > 0x2060000:
                params['timeout'] = 4
            if (sys.hexversion >= 0x2070900) and self.ssl:
                import ssl as ssllib
                params['context'] = ssllib._create_unverified_context()
            h = conn_factory(connect_host, connect_port,**params)
            if self.debuglevel <= 10:
                if self.debuglevel > 1:
                    h.set_debuglevel(self.debuglevel)
            try:
                self.log.info('Sending %s %s' % (method, path))
                h.request(method, query_path, headers=headers)
            except socket.error:
                self.log.warn('Could not initialize connection to %s' % self.target)
                return
            self.requestnumber += 1

            response = h.getresponse()
            responsebody = response.read()
            h.close()
            r = response, responsebody
        except (socket.error, socket.timeout, httplib.BadStatusLine):
            self.log.warn('Hey.. they closed our connection!')
            r = None
        finally:
            self.proxy.terminate()

        return r


    def querycrawler(self, path=None, curdepth=0, maxdepth=1):
        self.log.debug('Crawler is visiting %s' % path)
        localcrawlpaths = list()
        if curdepth > maxdepth:
            self.log.info('maximum depth %s reached' % maxdepth)
            return
        r = self.request(path=path)
        if r is None:
            return
        response, responsebody = r
        try:
            soup = BeautifulSoup(responsebody)
        except:
            self.log.warn('could not parse the response body')
            return
        tags = soup('a')
        for tag in tags:
            try:
                href = tag["href"]
                if href is not None:
                    tmpu = urlparse(href)
                    if (tmpu[1] != '') and (self.target != tmpu[1]):
                        # not on the same domain name .. ignore
                        self.log.debug('Ignoring link because it is not on the same site %s' % href)
                        continue
                    if tmpu[0] not in ['http', 'https', '']:
                        self.log.debug('Ignoring link because it is not an http uri %s' % href)
                        continue
                    path = tmpu[2]
                    if not path.startswith('/'):
                        path = '/' + path
                    if len(tmpu[4]) > 0:
                        # found a query .. thats all we need                                                
                        location = urlunparse(('', '', path, tmpu[3], tmpu[4], ''))
                        self.log.info('Found query %s' % location)
                        return href
                    if path not in self.crawlpaths:
                        href = unquote(path)
                        self.log.debug('adding %s for crawling' % href)
                        self.crawlpaths.append(href)
                        localcrawlpaths.append(href)
            except KeyError:
                pass
        for nextpath in localcrawlpaths:
            r = self.querycrawler(path=nextpath, curdepth=curdepth + 1, maxdepth=maxdepth)
            if r:
                return r

    def _parse_proxy(self, proxy):
        parts = urlparse(proxy)
        if not parts.scheme or not parts.netloc:
            raise Exception("Invalid proxy specified, scheme required")
        
        netloc = parts.netloc.split(":")
        if len(netloc) != 2:
            raise Exception("Proxy port unspecified")

        try:
            if parts.scheme == "socks5":
                if socks is None:
                    raise Exception("socks5 proxy requires PySocks")

                return Socks5Proxy(netloc[0], int(netloc[1]))
            elif parts.scheme == "http":
                return HttpProxy(netloc[0], int(netloc[1]))
            else:
                raise Exception("Unsupported proxy scheme")
        except ValueError:
            raise Exception("Invalid port number")



def scrambledheader(header):
    c = 'connection'
    if len(header) != len(c):
        return False
    if header == c:
        return False
    for character in c:
        if c.count(character) != header.count(character):
            return False
    return True

