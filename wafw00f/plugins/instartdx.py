#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Instart DX (Instart Logic)'


def is_waf(self):
    schema1 = [
        self.matchHeader(('X-Instart-Request-ID', '.+')),
        self.matchHeader(('X-Instart-Cache', '.+')),
        self.matchHeader(('X-Instart-WL', '.+'))
    ]
    schema2 = [
        self.matchContent(r'the requested url was rejected'),
        self.matchContent(r'please consult with your administrator'),
        self.matchContent(r'your support id is')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False