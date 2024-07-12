#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Gocache (Gocache)'

def is_waf(self):
    if self.matchContent(r'gocache\-error\-page'):
        return True

    return False
