#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'PT Application Firewall (Positive Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<h1.{0,10}?Forbidden'),
        self.matchContent(r'<pre>Request.ID:.{0,10}?\d{4}\-(\d{2})+.{0,35}?pre>')
    ]
    if all(i for i in schemes):
        return True
    return False
