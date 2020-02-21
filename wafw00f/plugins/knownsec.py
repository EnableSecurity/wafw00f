#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'KS-WAF (KnownSec)'


def is_waf(self):
    schemes = [
        self.matchContent(r'/ks[-_]waf[-_]error\.png')
    ]
    if any(i for i in schemes):
        return True
    return False