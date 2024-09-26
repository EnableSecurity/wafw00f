#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Safeline (Chaitin Tech.)'


def is_waf(self):
    if self.matchContent(r'safeline|<!\-\-\sevent id:'):
        return True

    return False
