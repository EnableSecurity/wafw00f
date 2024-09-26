#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Incapsula (Imperva Inc.)'


def is_waf(self):
    if self.matchCookie(r'^incap_ses.*?='):
        return True

    if self.matchCookie(r'^visid_incap.*?='):
        return True

    if self.matchContent(r'incapsula incident id'):
        return True

    if self.matchContent(r'powered by incapsula'):
        return True

    if self.matchContent(r'/_Incapsula_Resource'):
        return True

    return False
