#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'PowerCDN (PowerCDN)'


def is_waf(self):
    if self.matchHeader(('Via', r'(.*)?powercdn.com(.*)?')):
        return True

    if self.matchHeader(('X-Cache', r'(.*)?powercdn.com(.*)?')):
        return True

    if self.matchHeader(('X-CDN', r'PowerCDN')):
        return True

    return False
