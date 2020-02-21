#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Armor Defense (Armor)'


def is_waf(self):
    schemes = [
        self.matchContent(r'blocked by website protection from armor'),
        self.matchContent(r'please create an armor support ticket')
    ]
    if any(i for i in schemes):
        return True
    return False