#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ChinaCache Load Balancer (ChinaCache)'


def is_waf(self):
    if self.matchHeader(('Powered-By-ChinaCache', '.+')):
        return True

    return False
