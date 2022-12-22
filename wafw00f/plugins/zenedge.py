#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Zenedge (Zenedge)'


def is_waf(self):
    if self.matchHeader(('Server', 'ZENEDGE')):
        return True

    if self.matchHeader(('X-Zen-Fury', r'.+?')):
        return True

    if self.matchContent(r'/__zenedge/'):
        return True

    return False
