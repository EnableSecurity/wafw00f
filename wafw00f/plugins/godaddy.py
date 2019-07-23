#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'GoDaddy Website Protection (GoDaddy)'


def is_waf(self):
    schemes = [
        self.matchContent(r'GoDaddy.security.+access.denied'),
        self.matchContent(r'Access.denied.+GoDaddy.website.firewall')
    ]
    if any(i for i in schemes):
        return True
    return False