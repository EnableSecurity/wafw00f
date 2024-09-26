#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ZScaler (Accenture)'


def is_waf(self):
    if self.matchHeader(('Server', r'ZScaler')):
        return True

    if self.matchContent(r"Access Denied.{0,10}?Accenture Policy"):
        return True

    if self.matchContent(r'policies\.accenture\.com'):
        return True

    if self.matchContent(r'login\.zscloud\.net/img_logo_new1\.png'):
        return True

    if self.matchContent(r'Zscaler to protect you from internet threats'):
        return True

    if self.matchContent(r"Internet Security by ZScaler"):
        return True

    if self.matchContent(r"Accenture.{0,10}?webfilters indicate that the site likely contains"):
        return True

    return False
