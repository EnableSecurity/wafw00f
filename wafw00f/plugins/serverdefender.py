#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ServerDefender VP (Port80 Software)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Pint', r'p(ort\-)?80'))
    ]
    if any(i for i in schemes):
        return True
    return False