#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'MaxCDN (MaxCDN)'


def is_waf(self):
    if self.matchHeader(('X-CDN', r'maxcdn')):
        return True

    return False
