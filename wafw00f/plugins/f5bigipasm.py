#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AppSec Manager (F5 Networks)'


def is_waf(self):
    schema1 = [
        self.matchContent('the requested url was rejected'),
        self.matchContent('please consult with your administrator')
    ]

    schema2 = [
        self.matchCookie(r'^TS.+?')
    ]

    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False