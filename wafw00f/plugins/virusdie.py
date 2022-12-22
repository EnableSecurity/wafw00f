#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'VirusDie (VirusDie LLC)'


def is_waf(self):
    if self.matchContent(r"cdn\.virusdie\.ru/splash/firewallstop\.png"):
        return True

    if self.matchContent(r'copy.{0,10}?Virusdie\.ru'):
        return True

    return False
