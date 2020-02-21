#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'IndusGuard (Indusface)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'IF_WAF')),
        self.matchContent(r'This website is secured against online attacks. Your request was blocked')
    ]
    if any(i for i in schemes):
        return True
    return False