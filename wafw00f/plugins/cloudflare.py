#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudflare (Cloudflare Inc.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('server', 'cloudflare')),
        self.matchHeader(('server', 'cloudflare.nginx')),
        self.matchHeader(('cf-ray', '.+')),
        self.matchCookie('__cfduid')
    ]
    if any(i for i in schemes):
        return True
    return False