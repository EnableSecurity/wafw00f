#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Link11 WAAP (Link11)'

def is_waf(self):
    if check_schema_01(self):
        return True

    return False


def check_schema_01(self):
    if self.matchHeader(('server', 'rhino-core-shield')):
        return True

    return False
  
