#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yunjiasu (Baidu Cloud Computing)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'Yunjiasu(.+)?'))
    ]
    if any(i for i in schemes):
        return True
    return False