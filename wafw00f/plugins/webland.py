#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebLand (WebLand)'


def is_waf(self):
    if self.matchHeader(('Server', r'protected by webland')):
        return True

    return False
