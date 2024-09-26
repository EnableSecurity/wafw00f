#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DataPower (IBM)'


def is_waf(self):
    if self.matchHeader(('X-Backside-Transport', r'(OK|FAIL)')):
        return True

    return False
