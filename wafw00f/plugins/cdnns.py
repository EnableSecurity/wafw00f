#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CdnNS Application Gateway (CdnNs/WdidcNet)'


def is_waf(self):
    if self.matchContent(r'cdnnswaf application gateway'):
        return True

    return False
