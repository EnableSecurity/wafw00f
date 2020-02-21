#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SonicWall (Dell)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'SonicWALL')),
        self.matchContent(r"<(title|h\d{1})>Web Site Blocked"),
        self.matchContent(r'\+?nsa_banner')
    ]
    if any(i for i in schemes):
        return True
    return False