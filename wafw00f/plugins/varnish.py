#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Varnish (OWASP)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Request rejected by xVarnish\-WAF')
    ]
    if any(i for i in schemes):
        return True
    return False