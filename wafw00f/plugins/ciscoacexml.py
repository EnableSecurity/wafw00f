#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ACE XML Gateway (Cisco)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'ACE XML Gateway'))
    ]
    if any(i for i in schemes):
        return True
    return False