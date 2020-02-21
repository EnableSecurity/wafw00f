#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Jiasule (Jiasule)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'jiasule\-waf')),
        self.matchCookie(r'^jsl_tracking(.+)?='),
        self.matchCookie(r'__jsluid='),
        self.matchContent(r'notice\-jiasule'),
        self.matchContent(r'static\.jiasule\.com')
    ]
    if any(i for i in schemes):
        return True
    return False