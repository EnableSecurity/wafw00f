#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'eEye SecureIIS (BeyondTrust)'


def is_waf(self):
    if self.matchContent(r'SecureIIS is an internet security application'):
        return True

    if self.matchContent(r'Download SecureIIS Personal Edition'):
        return True

    if self.matchContent(r'https?://www\.eeye\.com/Secure\-?IIS'):
        return True

    return False
