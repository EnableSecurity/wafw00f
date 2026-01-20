#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiGuard (Fortinet)'

def is_waf(self):
    if check_schema(self):
        return True

    return False

def check_schema(self):
    if self.matchContent('FortiGuard Intrusion Prevention'):
        return True

    if self.matchContent('//globalurl.fortinet.net'):
        return True

    if self.matchContent('<title>Web Filter Violation'):
        return True
    
    if self.matchContent('Web Filter Block Override'):
        return True

    return False
