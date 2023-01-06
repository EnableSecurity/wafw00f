#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SiteGuard (Sakura Inc.)'


def is_waf(self):
    if self.matchContent(r"Powered by SiteGuard"):
        return True

    if self.matchContent(r'The server refuse to browse the page'):
        return True

    return False
