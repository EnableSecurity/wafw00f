#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ASP.NET Generic (Microsoft)'


def is_waf(self):
    if self.matchContent(r'iis (\d+.)+?detailed error'):
        return True

    if self.matchContent(r'potentially dangerous request querystring'):
        return True

    if self.matchContent(r'application error from being viewed remotely (for security reasons)?'):
        return True

    if self.matchContent(r'An application error occurred on the server'):
        return True

    return False
