#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DataPower (IBM)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Backside-Transport', r'(OK|FAIL)'))
    ]
    if any(i for i in schemes):
        return True
    return False