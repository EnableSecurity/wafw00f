#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Tencent Cloud Firewall (Tencent Technologies)'


def is_waf(self):
    if self.matchContent(r'waf\.tencent\-?cloud\.com/'):
        return True

    return False
