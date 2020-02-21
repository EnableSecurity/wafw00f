#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Nemesida (PentestIt)'


def is_waf(self):
    schemes = [
        self.matchContent(r'@?nemesida(\-security)?\.com'),
        self.matchContent(r'Suspicious activity detected.{0,10}?Access to the site is blocked'),
        self.matchContent(r'nwaf@'),
        self.matchStatus(222)
    ]
    if any(i for i in schemes):
        return True
    return False