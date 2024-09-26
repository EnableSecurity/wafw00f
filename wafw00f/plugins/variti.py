#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Variti (Variti)'

def is_waf(self):
    if self.matchHeader(('Server', r'Variti(?:\/[a-z0-9\.\-]+)?')):
        return True

    return False
