#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ZScaler (Accenture)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'ZScaler')),
        self.matchContent(r"Access Denied.{0,10}?Accenture Policy"),
        self.matchContent(r'policies\.accenture\.com'),
        self.matchContent(r'login\.zscloud\.net/img_logo_new1\.png'),
        self.matchContent(r'Zscaler to protect you from internet threats'),
        self.matchContent(r"Internet Security by ZScaler"),
        self.matchContent(r"Accenture.{0,10}?webfilters indicate that the site likely contains")
    ]
    if any(i for i in schemes):
        return True
    return False