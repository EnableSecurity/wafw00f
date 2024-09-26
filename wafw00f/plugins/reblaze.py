#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Reblaze (Reblaze)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchCookie(r'^rbzid'):
        return True

    if self.matchHeader(('Server', 'Reblaze Secure Web Gateway')):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r'current session has been terminated'):
        return False

    if not self.matchContent(r'do not hesitate to contact us'):
        return False

    if not self.matchContent(r'access denied \(\d{3}\)'):
        return False

    return True
