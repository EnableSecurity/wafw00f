#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Puhui (Puhui)'


def is_waf(self):
    if self.matchHeader(('Server', r'Puhui[\-_]?WAF')):
        return True

    return False
