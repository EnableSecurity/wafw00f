#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'HyperGuard (Art of Defense)'


def is_waf(self):
    schemes = [
        self.matchCookie('^WODSESSION=')
    ]
    if any(i for i in schemes):
        return True
    return False