#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SecuPress WP Security (SecuPress)'


def is_waf(self):
    if self.matchContent(r'<(title|h\d{1})>SecuPress'):
        return True

    return False
