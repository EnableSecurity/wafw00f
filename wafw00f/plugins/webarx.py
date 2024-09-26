#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebARX (WebARX Security Solutions)'


def is_waf(self):
    if self.matchContent(r"WebARX.{0,10}?Web Application Firewall"):
        return True

    if self.matchContent(r"www\.webarxsecurity\.com"):
        return True

    if self.matchContent(r'/wp\-content/plugins/webarx/includes/'):
        return True

    return False
