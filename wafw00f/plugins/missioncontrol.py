#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Mission Control Shield (Mission Control)'


def is_waf(self):
    if self.matchHeader(('Server', 'Mission Control Application Shield')):
        return True

    return False
