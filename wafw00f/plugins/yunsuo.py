#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yunsuo (Yunsuo)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^yunsuo_session='),
        self.matchContent(r'class=\"yunsuologo\"')
    ]
    if any(i for i in schemes):
        return True
    return False