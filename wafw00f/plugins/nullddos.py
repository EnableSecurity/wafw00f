#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NullDDoS Protection (NullDDoS)'


def is_waf(self):
    if self.matchHeader(('Server', r'NullDDoS(.System)?')):
        return True

    return False
