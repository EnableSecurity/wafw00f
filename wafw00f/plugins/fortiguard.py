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
    # Use OR logic with strong signatures containing explicit FortiGuard/Fortinet branding
    # Generic "Web Filter" strings are avoided to prevent false positives
    if self.matchContent('FortiGuard Intrusion Prevention'):
        return True

    if self.matchContent('//globalurl.fortinet.net'):
        return True

    return False
