#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'TransIP Web Firewall (TransIP)'


def is_waf(self):
    if self.matchHeader(('X-TransIP-Backend', '.+')):
        return True

    if self.matchHeader(('X-TransIP-Balancer', '.+')):
        return True

    return False
