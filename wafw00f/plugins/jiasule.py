#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Jiasule (Jiasule)'


def is_waf(self):
    if self.matchHeader(('Server', r'jiasule\-waf')):
        return True

    if self.matchCookie(r'^jsl_tracking(.+)?='):
        return True

    if self.matchCookie(r'__jsluid='):
        return True

    if self.matchContent(r'notice\-jiasule'):
        return True

    if self.matchContent(r'static\.jiasule\.com'):
        return True

    return False
