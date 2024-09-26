#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Barracuda (Barracuda Networks)'


def is_waf(self):
    if self.matchCookie(r'^barra_counter_session='):
        return True

    if self.matchCookie(r'^BNI__BARRACUDA_LB_COOKIE='):
        return True

    if self.matchCookie(r'^BNI_persistence='):
        return True

    if self.matchCookie(r'^BN[IE]S_.*?='):
        return True

    if self.matchContent(r'Barracuda.Networks'):
        return True

    return False
