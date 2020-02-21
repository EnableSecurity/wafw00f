#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DynamicWeb Injection Check (DynamicWeb)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-403-Status-By', r'dw.inj.check'), attack=True),
        self.matchContent(r'by dynamic check(.{0,10}?module)?')
    ]
    if any(i for i in schemes):
        return True
    return False