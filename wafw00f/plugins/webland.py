#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebLand (WebLand)'


def is_waf(self):
    if self.matchHeader(('Server', r'protected by webland')):
        return True

    return False
