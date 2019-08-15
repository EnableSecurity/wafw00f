#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WTS-WAF (WTS)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'wts(.+)?')),
        self.matchContent(r"<h\d{1}>WTS-WAF"),
        self.matchContent(r'<title>WTS-WAF')
    ]
    if any(i for i in schemes):
        return True
    return False