#!/usr/bin/env python
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Azion Edge Firewall (Azion)'


def is_waf(self):
    if self.matchHeader(('x-azion-edge-pop', r'.+?')):
        return True

    if self.matchHeader(('x-azion-request-id', r'.+?')):
        return True

    return False
