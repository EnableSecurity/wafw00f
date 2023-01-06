#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ISA Server (Microsoft)'


def is_waf(self):
    if self.matchContent(r'The.{0,10}?(isa.)?server.{0,10}?denied the specified uniform resource locator \(url\)'):
        return True

    return False
