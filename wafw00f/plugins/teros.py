#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Teros (Citrix Systems)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^st8id=')
    ]
    if any(i for i in schemes):
        return True
    return False