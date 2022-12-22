#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'OnMessage Shield (BlackBaud)'


def is_waf(self):
    if self.matchHeader(('X-Engine', 'onMessage Shield')):
        return True

    if self.matchContent(r'Blackbaud K\-12 conducts routine maintenance'):
        return True

    if self.matchContent(r'onMessage SHEILD'):
        return True

    if self.matchContent(r'maintenance\.blackbaud\.com'):
        return True

    if self.matchContent(r'status\.blackbaud\.com'):
        return True

    return False
