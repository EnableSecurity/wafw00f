#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Reflected Networks (Reflected Networks)'


def is_waf(self):
    if self.matchContent(r'<b>Request ID</b>') and \
        self.matchContent(r'[0-9A-F]{8}-[0-9A-F]{18}-[0-9A-F]{6}') and \
        self.matchStatus(403) and \
        self.matchContent(r'content="Request is denied"') and \
        self.matchContent(r'<title>Forbidden</title>'):
        return True

    return False
