#!/usr/bin/env python
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Azure Application Gateway (Microsoft)'


def is_waf(self):
    if self.matchContent(r'Microsoft-Azure-Application-Gateway'):
        return True

    return False
