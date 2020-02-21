#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudflare (Cloudflare Inc.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('server', 'cloudflare')),
        self.matchHeader(('server', r'cloudflare[-_]nginx')),
        self.matchHeader(('cf-ray', r'.+?')),
        self.matchCookie('__cfduid')
    ]
    if any(i for i in schemes):
        return True
    return False