#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AzionCDN (AzionCDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'Azion([-_]CDN)?'))
    ]
    if any(i for i in schemes):
        return True
    return False