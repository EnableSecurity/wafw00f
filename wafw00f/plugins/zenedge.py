#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Zenedge (Zenedge)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'ZENEDGE')),
        self.matchHeader(('X-Zen-Fury', r'.+?')),
        self.matchContent(r'/__zenedge/')
    ]
    if any(i for i in schemes):
        return True
    return False