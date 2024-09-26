#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'URLScan (Microsoft)'


def is_waf(self):
    if self.matchContent(r"Rejected[-_]By[_-]UrlScan"):
        return True

    if self.matchContent(r'A custom filter or module.{0,4}?such as URLScan'):
        return True

    return False
