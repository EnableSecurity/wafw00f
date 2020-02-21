#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'West263 CDN (West263CDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Cache', r'WS?T263CDN'))
    ]
    if any(i for i in schemes):
        return True
    return False