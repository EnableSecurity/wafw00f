#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Anquanbao (Anquanbao)'


def is_waf(self):
    if self.matchHeader(('X-Powered-By-Anquanbao', '.+?')):
        return True

    if self.matchContent(r'aqb_cc/error/'):
        return True

    return False
