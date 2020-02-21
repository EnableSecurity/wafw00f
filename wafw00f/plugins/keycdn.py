#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'KeyCDN (KeyCDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'KeyCDN'))
    ]
    if any(i for i in schemes):
        return True
    return False