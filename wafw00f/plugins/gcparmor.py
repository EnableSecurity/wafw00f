#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Google Cloud App Armor (Google Cloud)'


def is_waf(self):
    if self.matchHeader(('Via', '1.1 google')):
        return True

    return False
