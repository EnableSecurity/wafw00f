#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'IndusGuard (Indusface)'


def is_waf(self):
    if self.matchHeader(('Server', r'IF_WAF')):
        return True

    if self.matchContent(r'This website is secured against online attacks. Your request was blocked'):
        return True

    return False
