#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Vercel WAF (Vercel)'


def is_waf(self):
    if self.matchContent(r'<title>Vercel Security Checkpoint</title>'):
        return True
    if self.matchContent(r'/vercel/security/'):
        return True

    return False
