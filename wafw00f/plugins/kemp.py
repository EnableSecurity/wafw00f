#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Kemp LoadMaster (Progress Software)'


def is_waf(self):
    if self.matchHeader(('X-ServedBy', 'KEMP-LM')) and \
        self.matchStatus(403) and \
        self.matchContent(r'<title>403 Forbidden</title>'):
        return True

    return False
