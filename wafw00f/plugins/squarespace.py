#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Squarespace (Squarespace)'


def is_waf(self):
    if self.matchHeader(('Server', 'Squarespace')):
        return True

    if self.matchCookie(r'^SS_ANALYTICS_ID='):
        return True

    if self.matchCookie(r'^SS_MATTR='):
        return True

    if self.matchCookie(r'^SS_MID='):
        return True

    if self.matchCookie(r'SS_CVT='):
        return True

    if self.matchContent(r'status\.squarespace\.com'):
        return True

    if self.matchContent(r'BRICK\-\d{2}'):
        return True

    return False
