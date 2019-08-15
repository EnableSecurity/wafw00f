#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Wordfence (Defiant)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'wf(\-)?WAF')),
        self.matchContent(r"(?s)Generated.by.Wordfence.at.+(Your computer's time)?"),
        self.matchContent(r'broke.one.of.(the.)?Wordfence.(advanced.)?blocking.rules'),
        self.matchContent(r"/plugins/wordfence")
    ]
    if any(i for i in schemes):
        return True
    return False