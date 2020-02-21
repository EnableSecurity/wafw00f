#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Safe3 Web Firewall (Safe3)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Safe3 Web Firewall')),
        self.matchHeader(('X-Powered-By', r'Safe3WAF/[\.0-9]+?')),
        self.matchContent(r'Safe3waf/[0-9\.]+?')
    ]
    if any(i for i in schemes):
        return True
    return False