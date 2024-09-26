#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AppWall (Radware)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchContent(r'CloudWebSec\.radware\.com'):
        return True

    if self.matchHeader(('X-SL-CompState', '.+')):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r'because we have detected unauthorized activity'):
        return False

    if not self.matchContent(r'<title>Unauthorized Request Blocked'):
        return False

    if not self.matchContent(r'if you believe that there has been some mistake'):
        return False

    if not self.matchContent(r'\?Subject=Security Page.{0,10}?Case Number'):
        return False

    return True
