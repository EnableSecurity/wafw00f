#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Varnish (OWASP)'


def is_waf(self):
    if self.matchContent(r'Request rejected by xVarnish\-WAF'):
        return True

    return False
