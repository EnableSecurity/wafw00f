#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Incapsula (Imperva Inc.)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^incap_ses.*?='),
        self.matchCookie(r'^visid_incap.*?='),
        self.matchContent(r'incapsula incident id'),
        self.matchContent(r'powered by incapsula'),
        self.matchContent(r'/_Incapsula_Resource')
    ]
    if any(i for i in schemes):
        return True
    return False