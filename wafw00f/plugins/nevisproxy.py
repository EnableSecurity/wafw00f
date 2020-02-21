#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NevisProxy (AdNovum)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^Navajo'),
        self.matchCookie(r'^NP_ID')
    ]
    if any(i for i in schemes):
        return True
    return False