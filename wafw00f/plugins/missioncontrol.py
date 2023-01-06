#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Mission Control Shield (Mission Control)'


def is_waf(self):
    if self.matchHeader(('Server', 'Mission Control Application Shield')):
        return True

    return False
