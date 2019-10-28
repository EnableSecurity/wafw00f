#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Fastly CDN (Fastly)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Fastly-Request-ID', r'\w+'))
    ]
    if any(i for i in schemes):
        return True
    return False