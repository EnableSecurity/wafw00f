#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'LiteSpeed (LiteSpeed Technologies)'


def is_waf(self):
    schema1 = [
        self.matchHeader(('Server', 'LiteSpeed')),
        self.matchStatus(403)
    ]
    schema2 = [
        self.matchContent(r'Proudly powered by litespeed web server'),
        self.matchContent(r'www\.litespeedtech\.com/error\-page')
    ]
    if all(i for i in schema1):
        return True
    if any(i for i in schema2):
        return True
    return False