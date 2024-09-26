#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BulletProof Security Pro (AITpro Security)'


def is_waf(self):
    if not self.matchContent(r'\+?bpsMessage'):
        return False

    if not self.matchContent(r'403 Forbidden Error Page'):
        return False

    if not self.matchContent(r'If you arrived here due to a search'):
        return False

    return True
