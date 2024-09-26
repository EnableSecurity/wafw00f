#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Edgecast (Verizon Digital Media)'


def is_waf(self):
    if self.matchHeader(('Server', r'^ECD(.+)?')):
        return True

    if self.matchHeader(('Server', r'^ECS(.*)?')):
        return True

    return False
