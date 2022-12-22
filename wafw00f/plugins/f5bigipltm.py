#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP Local Traffic Manager (F5 Networks)'


def is_waf(self):
    if self.matchCookie('^bigipserver'):
        return True

    if self.matchHeader(('X-Cnection', 'close'), attack=True):
        return True

    return False
