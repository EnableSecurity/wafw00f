#!/usr/bin/env python

"""
Copyright (C) 2009-2019 WAFW00F Developers.
See the file 'LICENSE' for copying permission
"""

import re
import sys
import time
import logging
import requests

try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse
try:
    from urllib import quote, unquote
except ImportError:
    from urllib.parse import quote, unquote

def_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',
                'DNT': '1',  # Do Not Track request header
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive'
        }
proxies = {}

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
        self.log = logging.getLogger('requester')
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
            self.log.info('Request Succeeded')
            self.log.debug('Headers: %s\n\n' % req.headers)
            self.log.debug('Content: %s\n\n' % req.content)
            self.requestnumber += 1
            return req
        except requests.exceptions.RequestException as e:
            self.log.error('Something went wrong %s' % (e.__str__()))

    def parseProxy(self, auth, proxies):
        pro = {}
        # User can submit multiple proxies with commas
        prox = proxies.split(',')
        for pr in prox:
            scheme = pr.split('://')[0].strip()
            proxy = pr.split('://')[1].strip()
            if auth:
                self.log.info('Switching to proxying with authentication')
                proxy = 'http://' + auth + '@' + proxy
            else:
                self.log.info('Switching to normal proxying without authentication')
                proxy = 'http://' + proxy
            if re.search(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', proxy):
                pro[scheme] = proxy
            else:
                self.log.error('Invalid proxy detected. Request routing disabled.')
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
