#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Janusec Application Gateway (Janusec)'


def is_waf(self):
    schemes = [
        self.matchContent(r'janusec application gateway')
    ]
    if any(i for i in schemes):
        return True
    return False