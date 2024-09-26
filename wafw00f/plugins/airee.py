#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AireeCDN (Airee)'


def is_waf(self):
    if self.matchHeader(('Server', 'Airee')):
        return True

    if self.matchHeader(('X-Cache', r'(\w+\.)?airee\.cloud')):
        return True

    if self.matchContent(r'airee\.cloud'):
        return True

    return False
