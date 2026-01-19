#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Baffin Bay (Mastercard)'


def is_waf(self):
    if self.matchHeader(('server', 'baffin-bay-inlet')):
        return True

    return False
