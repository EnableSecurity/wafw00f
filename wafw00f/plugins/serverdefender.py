#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ServerDefender VP (Port80 Software)'


def is_waf(self):
    if self.matchHeader(('X-Pint', r'p(ort\-)?80')):
        return True

    return False
