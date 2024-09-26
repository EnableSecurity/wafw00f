#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yunsuo (Yunsuo)'


def is_waf(self):
    if self.matchCookie(r'^yunsuo_session='):
        return True

    if self.matchContent(r'class=\"yunsuologo\"'):
        return True

    return False
