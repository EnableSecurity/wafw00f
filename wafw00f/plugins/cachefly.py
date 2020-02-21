#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CacheFly CDN (CacheFly)'


def is_waf(self):
    schemes = [
        self.matchHeader(('BestCDN', r'Cachefly')),
        self.matchCookie(r'^cfly_req.*=')
    ]
    if any(i for i in schemes):
        return True
    return False