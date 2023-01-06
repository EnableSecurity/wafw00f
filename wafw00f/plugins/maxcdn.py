#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'MaxCDN (MaxCDN)'


def is_waf(self):
    if self.matchHeader(('X-CDN', r'maxcdn')):
        return True

    return False
