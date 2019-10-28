#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'MaxCDN (MaxCDN)'


def is_waf(self):
    schemes = [
        self.matchCookie(('X-CDN', r'maxcdn'))
    ]
    if any(i for i in schemes):
        return True
    return False