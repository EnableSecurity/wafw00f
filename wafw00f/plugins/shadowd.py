#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Shadow Daemon (Zecure)'


def is_waf(self):
    if not self.matchContent(r"<h\d{1}>\d{3}.forbidden<.h\d{1}>"):
        return False

    if not self.matchContent(r"request forbidden by administrative rules"):
        return False

    return True
