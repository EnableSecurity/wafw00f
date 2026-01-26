#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Tencent Cloud Firewall (Tencent Technologies)'


def is_waf(self):
    if self.matchContent(r'waf\.tencent\-?cloud\.com/'):
        return True

    if self.matchContent(r'window\.location\.href.{1,3}?https?://waf.tencent(?:-?cloud)?.com/(?:403|501)page\.html'):
        return True

    return False
