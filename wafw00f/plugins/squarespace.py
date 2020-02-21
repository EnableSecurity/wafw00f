#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Squarespace (Squarespace)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Squarespace')),
        self.matchCookie(r'^SS_ANALYTICS_ID='),
        self.matchCookie(r'^SS_MATTR='),
        self.matchCookie(r'^SS_MID='),
        self.matchCookie(r'SS_CVT='),
        self.matchContent(r'status\.squarespace\.com'),
        self.matchContent(r'BRICK\-\d{2}')
    ]
    if any(i for i in schemes):
        return True 
    return False