#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = '360PanYun (360 Technologies)'


def is_waf(self):
    if self.matchHeader(('Server', r'panyun')):
        return True
    if self.matchHeader(('X-Panyun-Request-ID', r'.+?'), attack=True):
        return True
    if self.matchHeader(('X-Panyun-Error-Reason', r'.+?'), attack=True):
        return True
    if self.matchHeader(('X-Panyun-Error-Step', r'.+?'), attack=True):
        return True
    return False
