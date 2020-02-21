#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'PowerCDN (PowerCDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Via', r'(.*)?powercdn.com(.*)?')),
        self.matchHeader(('X-Cache', r'(.*)?powercdn.com(.*)?')),
        self.matchHeader(('X-CDN', r'PowerCDN'))
    ]
    if any(i for i in schemes):
        return True
    return False