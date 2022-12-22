#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Profense (ArmorLogic)'


def is_waf(self):
    if self.matchHeader(('Server', 'Profense')):
        return True

    if self.matchCookie(r'^PLBSID='):
        return True

    return False
