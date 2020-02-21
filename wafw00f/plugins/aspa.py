#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ASPA Firewall (ASPA Engineering Co.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'ASPA[\-_]?WAF')),
        self.matchHeader(('ASPA-Cache-Status', r'.+?'))
    ]
    if any(i for i in schemes):
        return True
    return False