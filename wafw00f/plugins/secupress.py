#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SecuPress WordPress Security (SecuPress)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<(title|h\d{1})>SecuPress'),
    ]
    if any(i for i in schemes):
        return True
    return False