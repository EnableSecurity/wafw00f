#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Beluga CDN (Beluga)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'Beluga')),
        self.matchCookie(r'^beluga_request_trail=')
    ]
    if any(i for i in schemes):
        return True
    return False