#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Azure Front Door (Microsoft)'


def is_waf(self):
    if self.matchHeader(('X-Azure-Ref', '.+?')):
        return True

    return False
