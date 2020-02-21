#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Wallarm (Wallarm Inc.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'nginx[\-_]wallarm'))
    ]
    if any(i for i in schemes):
        return True
    return False