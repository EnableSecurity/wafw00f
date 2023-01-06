#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ASPA Firewall (ASPA Engineering Co.)'


def is_waf(self):
    if self.matchHeader(('Server', r'ASPA[\-_]?WAF')):
        return True

    if self.matchHeader(('ASPA-Cache-Status', r'.+?')):
        return True

    return False
