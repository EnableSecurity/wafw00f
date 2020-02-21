#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ASP.NET Generic (Microsoft)'


def is_waf(self):
    schemes = [
        self.matchContent(r'iis (\d+.)+?detailed error'),
        self.matchContent(r'potentially dangerous request querystring'),
        self.matchContent(r'application error from being viewed remotely (for security reasons)?'),
        self.matchContent(r'An application error occurred on the server'),
    ]
    if any(i for i in schemes):
        return True
    return False