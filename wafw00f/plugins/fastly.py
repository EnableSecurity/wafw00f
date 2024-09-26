#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Fastly (Fastly CDN)'


def is_waf(self):
    if self.matchHeader(('X-Fastly-Request-ID', r'\w+')):
        return True

    return False
