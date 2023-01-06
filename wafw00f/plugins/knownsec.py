#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'KS-WAF (KnownSec)'


def is_waf(self):
    if self.matchContent(r'/ks[-_]waf[-_]error\.png'):
        return True

    return False
