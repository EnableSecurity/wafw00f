#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Mission Control Application Shield (Mission Control)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Mission.Control.Application.Shield'))
    ]
    if any(i for i in schemes):
        return True
    return False