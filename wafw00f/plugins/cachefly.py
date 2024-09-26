#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CacheFly CDN (CacheFly)'


def is_waf(self):
    if self.matchHeader(('BestCDN', r'Cachefly')):
        return True

    if self.matchCookie(r'^cfly_req.*='):
        return True

    return False
