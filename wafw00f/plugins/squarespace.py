#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Squarespace (Squarespace)'


def is_waf(self):
    schemes = [
        self.matchContent(r'(?s).+@.+?BRICK-50')
    ]
    if any(i for i in schemes):
        return True
    return False