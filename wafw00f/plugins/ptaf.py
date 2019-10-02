#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Positive Technologies Application Firewall (PT Security)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<h1.+?Forbidden'),
        self.matchContent(r'<pre>Request.ID:.+?\d{4}\-(\d{2})+.+?pre>')
    ]
    if all(i for i in schemes):
        return True
    return False