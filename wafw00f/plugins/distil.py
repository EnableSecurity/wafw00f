#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Distil (Distil Networks)'


def is_waf(self):
    if self.matchContent(r'cdn\.distilnetworks\.com/images/anomaly\.detected\.png'):
        return True

    if self.matchContent(r'distilCaptchaForm'):
        return True

    if self.matchContent(r'distilCallbackGuard'):
        return True

    return False
