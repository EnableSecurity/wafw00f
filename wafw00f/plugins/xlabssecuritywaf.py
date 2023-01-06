#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'XLabs Security WAF (XLabs)'


def is_waf(self):
    if self.matchHeader(('X-CDN', r'XLabs Security')):
        return True

    if self.matchHeader(('Secured', r'^By XLabs Security')):
        return True

    if self.matchHeader(('Server', r'XLabs[-_]?.?WAF'), attack=True):
        return True

    return False
