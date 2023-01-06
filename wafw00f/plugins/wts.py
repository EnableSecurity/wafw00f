#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WTS-WAF (WTS)'


def is_waf(self):
    if self.matchHeader(('Server', r'wts/[0-9\.]+?')):
        return True

    if self.matchContent(r"<(title|h\d{1})>WTS\-WAF"):
        return True

    return False
