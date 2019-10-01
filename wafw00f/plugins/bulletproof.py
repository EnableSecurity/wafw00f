#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BulletProof Security Pro (AITpro Security)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<div.+?id=.+?bpsMessage'),
        self.matchContent(r'(?s)403 Forbidden Error Page.+?If you arrived here due to a search')
    ]
    if any(i for i in schemes):
        return True
    return False