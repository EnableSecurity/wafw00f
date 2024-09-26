#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WP Cerber Security (Cerber Tech)'


def is_waf(self):
    if not self.matchContent(r'your request looks suspicious or similar to automated'):
        return False

    if not self.matchContent(r'our server stopped processing your request'):
        return False

    if not self.matchContent(r'We.re sorry.{0,10}?you are not allowed to proceed'):
        return False

    if not self.matchContent(r'requests from spam posting software'):
        return False

    if not self.matchContent(r'<title>403 Access Forbidden'):
        return False

    return True
