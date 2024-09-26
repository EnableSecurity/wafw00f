#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Nemesida (PentestIt)'


def is_waf(self):
    if self.matchContent(r'@?nemesida(\-security)?\.com'):
        return True

    if self.matchContent(r'Suspicious activity detected.{0,10}?Access to the site is blocked'):
        return True

    if self.matchContent(r'nwaf@'):
        return True

    if self.matchStatus(222):
        return True

    return False
