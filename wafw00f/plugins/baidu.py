#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yunjiasu (Baidu Cloud Computing)'


def is_waf(self):
    schemes = [

        # just added another signature
        self.matchHeader(('Server', r'Yunjiasu(.+)?')),
        self.matchHeader(('Server', 'yunjiasu-nginx'))
    ]
    if any(i for i in schemes):
        return True
    return False