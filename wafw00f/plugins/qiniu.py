#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Qiniu (Qiniu CDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Qiniu-CDN', r'\d+?'))
    ]
    if any(i for i in schemes):
        return True
    return False