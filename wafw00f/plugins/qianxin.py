#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Qianxin (Yunsuo)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'qianxin-waf')),
    ]
    if any(i for i in schemes):
        return True
    return False