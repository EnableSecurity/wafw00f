#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DotDefender (Applicure Technologies)'


def is_waf(self):
    if self.matchHeader(('X-dotDefender-denied', r'.+?'), attack=True):
        return True

    if self.matchContent(r'dotdefender blocked your request'):
        return True

    if self.matchContent(r'Applicure is the leading provider of web application security'):
        return True

    return False
