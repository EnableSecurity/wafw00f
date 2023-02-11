#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Variti (Variti)'


def is_waf(self):
    if self.matchHeader(('Server', r'VARITI')):
        return True

    return False
