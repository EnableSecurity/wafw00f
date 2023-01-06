#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'GoDaddy Website Protection (GoDaddy)'


def is_waf(self):
    if self.matchContent(r'GoDaddy (security|website firewall)'):
        return True

    return False
