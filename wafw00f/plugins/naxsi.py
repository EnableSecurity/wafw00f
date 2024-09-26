#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NAXSI (NBS Systems)'


def is_waf(self):
    if self.matchHeader(('X-Data-Origin', r'^naxsi(.+)?')):
        return True

    if self.matchHeader(('Server', r'naxsi(.+)?')):
        return True

    if self.matchContent(r'blocked by naxsi'):
        return True

    if self.matchContent(r'naxsi blocked information'):
        return True

    return False
