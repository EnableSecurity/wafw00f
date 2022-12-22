#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Teros (Citrix Systems)'


def is_waf(self):
    if self.matchCookie(r'^st8id='):
        return True

    return False
