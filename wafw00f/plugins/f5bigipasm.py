#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AppSec Manager (F5 Networks)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if self.matchCookie(r'^TS.+?'):
        return True

    return False


def check_schema_01(self):
    if not self.matchContent('the requested url was rejected'):
        return False

    if not self.matchContent('please consult with your administrator'):
        return False

    return True
