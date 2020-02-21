#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NAXSI (NBS Systems)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Data-Origin', r'^naxsi(.+)?')),
        self.matchHeader(('Server', r'naxsi(.+)?')),
        self.matchContent(r'blocked by naxsi'),
        self.matchContent(r'naxsi blocked information')
    ]
    if any(i for i in schemes):
        return True
    return False