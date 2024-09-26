#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Comodo cWatch (Comodo CyberSecurity)'


def is_waf(self):
    if self.matchHeader(('Server', r'Protected by COMODO WAF(.+)?')):
        return True

    return False
