#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'aeSecure (aeSecure)'


def is_waf(self):
    if self.matchHeader(('aeSecure-code', '.+?')):
        return True

    if self.matchContent(r'aesecure_denied\.png'):
        return True

    return False
