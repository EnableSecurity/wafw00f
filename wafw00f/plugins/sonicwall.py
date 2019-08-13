#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SonicWall (Dell)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'SonicWALL')),
        self.matchContent(r"<.+?>Web Site Blocked<.+>"),
        self.matchContent(r'\+?nsa_banner')
    ]
    if any(i for i in schemes):
        return True
    return False