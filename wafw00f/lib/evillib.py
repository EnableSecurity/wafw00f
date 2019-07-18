#!/usr/bin/env python

"""
Copyright (C) 2006-2019 WAFW00F Developers.
See the file 'LICENSE' for copying permission
"""

import logging
import re, sys
import requests, time
import requests_cache
try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse
try:
    from urllib import quote, unquote
except ImportError:
    from urllib.parse import quote, unquote

requests_cache.install_cache('wafw00f', backend='sqlite', expire_after=300)

def_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',
                'DNT': '1',  # Do Not Track request header
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive'
        }
proxies = {}
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
                  '9': '%uff19'
            }

def bruteForceAscii(ourstr):
    listourstr = list(ourstr)
    for pos in range(len(ourstr)):
        for i in range(256):
            newlistourstr = listourstr[:]
            newlistourstr[pos] = chr(i)
            yield (quote(''.join(newlistourstr)))

def nullify(ourstr):
    newstr = str()
    for character in ourstr:
        newstr += character + "\x00"
    return quote(newstr)

def replaceChars(ourstr, origchar, newchar):
    newstr = ourstr.replace(origchar, newchar)
    return newstr

def nullifySpaces(ourstr):
    return quote(replaceChars(ourstr, ' ', '\x00'))

def slashSpaces(ourstr):
    return replaceChars(ourstr, ' ', '/')

def tabifySpaces(ourstr):
    return replaceChars(ourstr, ' ', '\t')

def crlfSpaces(ourstr):
    return replaceChars(ourstr, ' ', '\n')

def backslashQuotes(ourstr):
    return replaceChars(ourstr, "'", "\''")

def urlParser(target):
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

class waftoolsengine:
    def __init__(self, target='https://example.com', port=None, debuglevel=0, path='/', proxy=None, 
                redir=True, auth=None, head=None):
        self.target = target
        self.debuglevel = debuglevel
        self.requestnumber = 0
        self.path = path
        self.redirectno = 0
        self.allowredir = redir
        if port:
            self.target = self.target + ':' + str(port)
        if not head:
            self.headers = def_headers
        else:
            self.headers = head
        if proxy:
            self.proxy = self.parseProxy(auth, proxy)
        else:
            self.proxy = proxy

    def Request(self, path=None, params={}, delay=0, timeout=7):
        try:
            time.sleep(delay)
            req = requests.get(self.target, proxies=self.proxy, headers=self.headers, timeout=timeout,
                    allow_redirects=self.allowredir, params=params)
            return req
        except requests.exceptions.RequestException as e:
            print('Something went wrong %s' % (e.__str__()))

    def parseProxy(self, auth, proxies):
        pro = {}
        # User can submit multiple proxies with commas
        prox = proxies.split(',')
        for pr in prox:
            scheme = pr.split('://')[0].strip()
            proxy = pr.split('://')[1].strip()
            if auth:
                proxy = 'http://' + auth + '@' + proxy
            else:
                proxy = 'http://' + proxy
            if re.search(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', proxy):
                pro[scheme] = proxy
            else:
                print('Invalid proxy detected. Request routing disabled.')
        return pro

def scrambledHeader(header):
    c = 'connection'
    if len(header) != len(c):
        return False
    if header == c:
        return False
    for character in c:
        if c.count(character) != header.count(character):
            return False
    return True
