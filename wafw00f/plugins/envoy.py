#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Envoy'


def is_waf(self):
    if self.matchHeader(('server', 'envoy')):
        return True

    return False
