#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AnYu (AnYu Technologies)'


def is_waf(self):
    if self.matchContent(r'anyu.{0,10}?the green channel'):
        return True

    if self.matchContent(r'your access has been intercepted by anyu'):
        return True

    return False
