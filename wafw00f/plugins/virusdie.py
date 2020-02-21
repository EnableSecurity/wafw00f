#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'VirusDie (VirusDie LLC)'


def is_waf(self):
    schemes = [
        self.matchContent(r"cdn\.virusdie\.ru/splash/firewallstop\.png"),
        self.matchContent(r'copy.{0,10}?Virusdie\.ru')
    ]
    if any(i for i in schemes):
        return True
    return False