#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

import re
import sys
import time
import logging
from copy import copy

import requests
import urllib3
try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse
try:
    from urllib import quote, unquote
except ImportError:
    from urllib.parse import quote, unquote
# For requests < 2.16, this should be used.
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# For requests >= 2.16, this is the convention 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def_headers = {'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.9',
               'DNT'            : '1',  # Do Not Track request header
               'User-Agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3770.100 Safari/537.36',
               'Upgrade-Insecure-Requests': '1' #
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
    def __init__(self, target='https://example.com', debuglevel=0, path='/', proxies=None, 
                redir=True, head=None):
        self.target = target
        self.debuglevel = debuglevel
        self.requestnumber = 0
        self.path = path
        self.redirectno = 0
        self.allowredir = redir
        self.proxies = proxies
        self.log = logging.getLogger('wafw00f')
        if head:
            self.headers = head
        else:
            self.headers = copy(def_headers) #copy object by value not reference. Fix issue #90

    def Request(self, headers=None, path=None, params={}, delay=0, timeout=7):
        try:
            time.sleep(delay)
            if not headers: 
                h = self.headers
            else: h = headers
            req = requests.get(self.target, proxies=self.proxies, headers=h, timeout=timeout,
                    allow_redirects=self.allowredir, params=params, verify=False)
            self.log.info('Request Succeeded')
            self.log.debug('Headers: %s\n' % req.headers)
            self.log.debug('Content: %s\n' % req.content)
            self.requestnumber += 1
            return req
        except requests.exceptions.RequestException as e:
            self.log.error('Something went wrong %s' % (e.__str__()))
