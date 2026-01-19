#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ThreatX (A10 Networks)'


def is_waf(self):
    if self.matchHeader(('X-Request-Id', r'.*')) and \
       self.matchContent(r"^Forbidden - ID: ([a-fA-F0-9]{32})$") and \
       self.matchStatus(403):
        return True

    return False
