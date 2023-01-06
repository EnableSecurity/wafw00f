#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Wallarm (Wallarm Inc.)'


def is_waf(self):
    if self.matchHeader(('Server', r'nginx[\-_]wallarm')):
        return True

    return False
