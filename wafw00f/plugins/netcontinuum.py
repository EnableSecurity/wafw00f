#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NetContinuum (Barracuda Networks)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^NCI__SessionId=')
    ]
    if any(i for i in schemes):
        return True
    return False