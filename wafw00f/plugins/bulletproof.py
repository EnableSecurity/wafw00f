#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BulletProof Security Pro (AITpro Security)'


def is_waf(self):
    schemes = [
        self.matchContent(r'\+?bpsMessage'),
        self.matchContent(r'403 Forbidden Error Page'),
        self.matchContent(r'If you arrived here due to a search')
    ]
    if all(i for i in schemes):
        return True
    return False