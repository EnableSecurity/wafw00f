#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ACE XML Gateway (Cisco)'


def is_waf(self):
    if self.matchHeader(('Server', 'ACE XML Gateway')):
        return True

    return False
