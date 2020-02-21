#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'LimeLight CDN (LimeLight)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^limelight'),
        self.matchCookie(r'^l[mg]_sessid=')
    ]
    if any(i for i in schemes):
        return True
    return False 