#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DDoS-GUARD (DDOS-GUARD CORP.)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^__ddg1.*?='),
        self.matchCookie(r'^__ddg2.*?='),
        self.matchCookie(r'^__ddgid.*?='),
        self.matchCookie(r'^__ddgmark.*?='),
        self.matchHeader(('Server', 'ddos-guard')),
    ]
    if any(i for i in schemes):
        return True
    return False