#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'LiteSpeed (LiteSpeed Technologies)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchHeader(('Server', 'LiteSpeed')):
        return False

    if not self.matchStatus(403):
        return False

    return True


def check_schema_02(self):
    if self.matchContent(r'Proudly powered by litespeed web server'):
        return True

    if self.matchContent(r'www\.litespeedtech\.com/error\-page'):
        return True

    return False
