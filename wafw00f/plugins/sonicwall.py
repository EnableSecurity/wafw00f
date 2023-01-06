#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SonicWall (Dell)'


def is_waf(self):
    if self.matchHeader(('Server', 'SonicWALL')):
        return True

    if self.matchContent(r"<(title|h\d{1})>Web Site Blocked"):
        return True

    if self.matchContent(r'\+?nsa_banner'):
        return True

    return False
