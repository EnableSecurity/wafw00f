#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Squarespace (Squarespace)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'BRICK-\d{2}'),
        self.matchContent(r'[0-9a-z]+{8}/[0-9a-z]+{8}')
    ]
    schema2 = [
        self.matchHeader(('Server', 'Squarespace')),
        self.matchCookie(r'^SS_ANALYTICS_ID='),
        self.matchCookie(r'^SS_MATTR='),
        self.matchCookie(r'^SS_MID='),
        self.matchCookie(r'SS_CVT='),
        self.matchContent(r'status\.squarespace\.com')
    ]
    if any(i for i in schema2):
        return True 
    if all(i for i in schema1):
        return True
    return False