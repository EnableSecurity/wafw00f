#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Beluga CDN (Beluga)'


def is_waf(self):
    if self.matchHeader(('Server', r'Beluga')):
        return True

    if self.matchCookie(r'^beluga_request_trail='):
        return True

    return False
