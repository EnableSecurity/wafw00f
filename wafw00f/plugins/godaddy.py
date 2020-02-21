#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'GoDaddy Website Protection (GoDaddy)'


def is_waf(self):
    schemes = [
        self.matchContent(r'GoDaddy (security|website firewall)')
    ]
    if any(i for i in schemes):
        return True
    return False