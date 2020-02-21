#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebSEAL (IBM)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'WebSEAL')),
        self.matchContent(r"This is a WebSEAL error message template file"),
        self.matchContent(r"WebSEAL server received an invalid HTTP request")
    ]
    if any(i for i in schemes):
        return True
    return False