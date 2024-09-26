#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SiteGround (SiteGround)'


def is_waf(self):
    if self.matchContent(r"Our system thinks you might be a robot!"):
        return True

    if self.matchContent(r'access is restricted due to a security rule'):
        return True

    return False
