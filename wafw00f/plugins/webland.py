#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebLand (WebLand)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'protected by webland'))
    ]
    if any(i for i in schemes):
        return True
    return False