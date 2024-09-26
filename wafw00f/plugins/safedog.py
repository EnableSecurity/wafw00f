#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Safedog (SafeDog)'


def is_waf(self):
    if self.matchCookie(r'^safedog\-flow\-item='):
        return True

    if self.matchHeader(('Server', 'Safedog')):
        return True

    if self.matchContent(r'safedogsite/broswer_logo\.jpg'):
        return True

    if self.matchContent(r'404\.safedog\.cn/sitedog_stat.html'):
        return True

    if self.matchContent(r'404\.safedog\.cn/images/safedogsite/head\.png'):
        return True

    return False
