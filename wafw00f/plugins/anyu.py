#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AnYu (AnYu Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'anyu.+?the.green.channel'),
        self.matchContent(r'sorry.+?your.access.has.been.intercepted.by.anyu')
        ]
    if any(i for i in schemes):
        return True
    return False