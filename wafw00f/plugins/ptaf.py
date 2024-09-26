#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'PT Application Firewall (Positive Technologies)'


def is_waf(self):
    if not self.matchContent(r'<h1.{0,10}?Forbidden'):
        return False

    if not self.matchContent(r'<pre>Request.ID:.{0,10}?\d{4}\-(\d{2})+.{0,35}?pre>'):
        return False

    return True
