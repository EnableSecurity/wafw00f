#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SquidProxy IDS (SquidProxy)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'squid(/[0-9\.]+)?')),
        self.matchContent(r'Access control configuration prevents your request')
        ]
    if all(i for i in schemes):
        return True
    return False