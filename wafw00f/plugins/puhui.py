#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Puhui (Puhui)'


def is_waf(self):
    if self.matchHeader(('Server', r'Puhui[\-_]?WAF')):
        return True

    return False
