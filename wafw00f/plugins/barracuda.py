#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Barracuda Application Firewall (Barracuda Networks)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^barra_counter_session='),
        self.matchCookie(r'^BNI__BARRACUDA_LB_COOKIE='),
        self.matchCookie(r'^BNI_persistence='),
        self.matchCookie(r'^BN[IE]S_.*?='),
        self.matchContent(r'Barracuda.Networks')
    ]
    if any(i for i in schemes):
        return True
    return False