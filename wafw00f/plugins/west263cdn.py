#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'West263 CDN (West263CDN)'


def is_waf(self):
    if self.matchHeader(('X-Cache', r'WS?T263CDN')):
        return True

    return False
