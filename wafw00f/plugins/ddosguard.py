#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DDoS-GUARD (DDOS-GUARD CORP.)'


def is_waf(self):
    if self.matchCookie(r'^__ddg1.*?='):
        return True

    if self.matchCookie(r'^__ddg2.*?='):
        return True

    if self.matchCookie(r'^__ddgid.*?='):
        return True

    if self.matchCookie(r'^__ddgmark.*?='):
        return True

    if self.matchHeader(('Server', 'ddos-guard')):
        return True

    return False
