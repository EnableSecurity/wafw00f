#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Secure Entry (United Security Providers)'


def is_waf(self):
    if self.matchHeader(('Server', 'Secure Entry Server')):
        return True

    return False
