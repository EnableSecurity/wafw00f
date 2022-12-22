#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NexusGuard Firewall (NexusGuard)'


def is_waf(self):
    if self.matchContent(r'Powered by Nexusguard'):
        return True

    if self.matchContent(r'nexusguard\.com/wafpage/.+#\d{3};'):
        return True

    return False
