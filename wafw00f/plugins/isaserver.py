#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ISA Server (Microsoft)'


def is_waf(self):
    schemes = [
        self.matchContent(r'The.+?(isa.)?server.+?denied the specified uniform resource locator \(url\)'),
    ]
    if any(i for i in schemes):
        return True
    return False