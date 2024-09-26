#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Janusec Application Gateway (Janusec)'


def is_waf(self):
    if self.matchContent(r'janusec application gateway'):
        return True

    return False
