#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DotDefender (Applicure Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-dotDefender-denied', r'.+?'), attack=True),
        self.matchContent(r'dotdefender blocked your request'),
        self.matchContent(r'Applicure is the leading provider of web application security')
    ]
    if any(i for i in schemes):
        return True
    return False