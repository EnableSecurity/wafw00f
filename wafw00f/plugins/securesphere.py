#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SecureSphere (Imperva Inc.)'


def is_waf(self):
    if not self.matchContent(r'<(title|h2)>Error'):
        return False

    if not self.matchContent(r'The incident ID is'):
        return False

    if not self.matchContent(r"This page can't be displayed"):
        return False

    if not self.matchContent(r'Contact support for additional information'):
        return False

    return True
