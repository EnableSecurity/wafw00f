#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'aeSecure (aeSecure)'


def is_waf(self):
    schemes = [
        self.matchHeader(('aeSecure-code', '.+?')),
        self.matchContent(r'aesecure_denied\.png')
    ]
    if any(i for i in schemes):
        return True
    return False