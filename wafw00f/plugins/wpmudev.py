#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wpmudev WAF (Incsub)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'href="http(s)?.\/\/wpmudev.com\/.{0,15}?'),
        self.matchContent(r'Click on the Logs tab, then the WAF Log.'),
        self.matchContent(r'Choose your site from the list'),
        self.matchStatus(403)
    ]
    schema2 = [
        self.matchContent(r'<h1>Whoops, this request has been blocked!'),
        self.matchContent(r'This request has been deemed suspicious'),
        self.matchContent(r'possible attack on our servers.'),
        self.matchStatus(403)
    ]
    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False
