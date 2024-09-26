#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Anquanbao (Anquanbao)'


def is_waf(self):
    if self.matchHeader(('X-Powered-By-Anquanbao', '.+?')):
        return True

    if self.matchContent(r'aqb_cc/error/'):
        return True

    return False
