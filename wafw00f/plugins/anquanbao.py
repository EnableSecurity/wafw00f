#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Anquanbao (Anquanbao)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Powered-By-Anquanbao', '.+?')),
        self.matchContent(r'aqb_cc/error/')
        ]
    if any(i for i in schemes):
        return True
    return False