#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Azure Front Door (Microsoft)'


def is_waf(self):
    if self.matchHeader(('X-Azure-Ref', '.+?')):
        return True

    return False
