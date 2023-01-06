#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Barikode (Ethic Ninja)'


def is_waf(self):
    if self.matchContent(r'<strong>barikode<.strong>'):
        return True

    return False
