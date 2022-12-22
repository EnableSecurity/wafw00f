#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'PerimeterX (PerimeterX)'


def is_waf(self):
    if self.matchContent(r'www\.perimeterx\.(com|net)/whywasiblocked'):
        return True

    if self.matchContent(r'client\.perimeterx\.(net|com)'):
        return True

    if self.matchContent(r'denied because we believe you are using automation tools'):
        return True

    return False
