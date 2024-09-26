#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Qiniu (Qiniu CDN)'


def is_waf(self):
    if self.matchHeader(('X-Qiniu-CDN', r'\d+?')):
        return True

    return False
