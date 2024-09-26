#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BitNinja (BitNinja)'


def is_waf(self):
    if self.matchContent(r'Security check by BitNinja'):
        return True

    if self.matchContent(r'Visitor anti-robot validation'):
        return True

    return False
