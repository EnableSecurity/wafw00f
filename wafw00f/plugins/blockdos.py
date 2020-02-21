#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BlockDoS (BlockDoS)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'blockdos\.net'))
    ]
    if any(i for i in schemes):
        return True
    return False