#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Safe3 Web Firewall (Safe3)'


def is_waf(self):
    if self.matchHeader(('Server', 'Safe3 Web Firewall')):
        return True

    if self.matchHeader(('X-Powered-By', r'Safe3WAF/[\.0-9]+?')):
        return True

    if self.matchContent(r'Safe3waf/[0-9\.]+?'):
        return True

    return False
