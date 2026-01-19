#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Fastly (Fastly CDN)'


def is_waf(self):
    if self.matchHeader(('X-Fastly-Request-ID', r'\w+')):
        return True

    if self.matchHeader(('X-Served-By', r'^cache-[a-z]{3}\d+-[A-Z]{3}')):
        return True

    return False
