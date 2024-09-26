#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WatchGuard (WatchGuard Technologies)'


def is_waf(self):
    if self.matchHeader(('Server', 'WatchGuard')):
        return True

    if self.matchContent(r"Request denied by WatchGuard Firewall"):
        return True

    if self.matchContent(r'WatchGuard Technologies Inc\.'):
        return True

    return False
