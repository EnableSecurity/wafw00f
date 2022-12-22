#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BlockDoS (BlockDoS)'


def is_waf(self):
    if self.matchHeader(('Server', r'blockdos\.net')):
        return True

    return False
