#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'HyperGuard (Art of Defense)'


def is_waf(self):
    if self.matchCookie('^WODSESSION='):
        return True

    return False
