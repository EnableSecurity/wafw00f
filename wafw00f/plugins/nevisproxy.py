#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NevisProxy (AdNovum)'


def is_waf(self):
    if self.matchCookie(r'^Navajo'):
        return True

    if self.matchCookie(r'^NP_ID'):
        return True

    return False
