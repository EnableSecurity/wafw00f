#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AppWall (Radware)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'CloudWebSec\.radware\.com'),
        self.matchHeader(('X-SL-CompState', '.+'))
    ]
    schema2 = [
        self.matchContent(r'because we have detected unauthorized activity'),
        self.matchContent(r'<title>Unauthorized Request Blocked'),
        self.matchContent(r'if you believe that there has been some mistake'),
        self.matchContent(r'\?Subject=Security Page.{0,10}?Case Number')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False