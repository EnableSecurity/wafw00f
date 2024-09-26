#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Armor Defense (Armor)'


def is_waf(self):
    if self.matchContent(r'blocked by website protection from armor'):
        return True

    if self.matchContent(r'please create an armor support ticket'):
        return True

    return False
