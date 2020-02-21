#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Huawei Cloud Firewall (Huawei)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^HWWAFSESID='),
        self.matchHeader(('Server', r'HuaweiCloudWAF')),
        self.matchContent(r'hwclouds\.com'),
        self.matchContent(r'hws_security@')
    ]
    if any(i for i in schemes):
        return True
    return False