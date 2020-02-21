#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DenyALL (Rohde & Schwarz CyberSecurity)'


def is_waf(self):
    schemes = [
        self.matchStatus(200),
        self.matchReason('Condition Intercepted')
    ]
    if all(i for i in schemes):
        return True
    return False