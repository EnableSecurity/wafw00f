#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'pkSecurity IDS (pkSec)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'pk.?Security.?Module'),
        self.matchContent(r'Security.Alert')
    ]
    schema2 = [
        self.matchContent(r'As this could be a potential hack attack'),
        self.matchContent(r'A safety critical (call|request) was (detected|discovered) and blocked'),
        self.matchContent(r'maximum number of reloads per minute and prevented access')
    ]
    if any(i for i in schema2):
        return True
    if all(i for i in schema1):
        return True
    return False