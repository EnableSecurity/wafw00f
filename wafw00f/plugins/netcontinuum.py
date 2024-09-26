#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NetContinuum (Barracuda Networks)'


def is_waf(self):
    if self.matchCookie(r'^NCI__SessionId='):
        return True

    return False
