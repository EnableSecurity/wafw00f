#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NinjaFirewall (NinTechNet)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>NinjaFirewall.{0,10}?\d{3}.forbidden'),
        self.matchContent(r'For security reasons?.{0,10}?it was blocked and logged')
    ]
    if all(i for i in schemes):
        return True
    return False