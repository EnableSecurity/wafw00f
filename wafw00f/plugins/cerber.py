#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WP Cerber Security (Cerber Tech)'


def is_waf(self):
    schemes = [
        self.matchContent(r'your request looks suspicious or similar to automated'),
        self.matchContent(r'our server stopped processing your request'),
        self.matchContent(r'We.re sorry.{0,10}?you are not allowed to proceed'),
        self.matchContent(r'requests from spam posting software'),
        self.matchContent(r'<title>403 Access Forbidden')
        ]
    if all(i for i in schemes):
        return True
    return False