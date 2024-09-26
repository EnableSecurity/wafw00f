#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudflare (Cloudflare Inc.)'


def is_waf(self):
    if self.matchHeader(('server', 'cloudflare')):
        return True

    if self.matchHeader(('server', r'cloudflare[-_]nginx')):
        return True

    if self.matchHeader(('cf-ray', r'.+?')):
        return True

    if self.matchCookie('__cfduid'):
        return True

    return False
