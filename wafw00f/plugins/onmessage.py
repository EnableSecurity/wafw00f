#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'OnMessage Shield (BlackBaud)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Engine', 'onMessage Shield')),
        self.matchContent(r'Blackbaud K\-12 conducts routine maintenance'),
        self.matchContent(r'onMessage SHEILD'),
        self.matchContent(r'maintenance\.blackbaud\.com'),
        self.matchContent(r'status\.blackbaud\.com')
    ]
    if any(i for i in schemes):
        return True
    return False