#!/usr/bin/env python3
'''
Copyright (C) 2023, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiGuard (Fortinet)'

def is_waf(self):
    if check_schema(self):
        return True

    return False

def check_schema(self):
    if not self.matchContent('FortiGuard Intrusion Prevention'):
        return False

    if not self.matchContent('//globalurl.fortinet.net'):
        return False

    if not self.matchContent('<title>Web Filter Violation'):
        return False
      
    return True
