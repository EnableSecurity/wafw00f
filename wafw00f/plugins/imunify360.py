#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Imunify360 (CloudLinux)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'imunify360.{0,10}?')),
        self.matchContent(r'protected.by.{0,10}?imunify360'),
        self.matchContent(r'powered.by.{0,10}?imunify360'),
        self.matchContent(r'imunify360.preloader')
    ]
    if any(i for i in schemes):
        return True
    return False