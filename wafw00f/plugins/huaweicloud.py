#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Huawei Cloud Firewall (Huawei)'


def is_waf(self):
    schemes = [
        self.matchContent(r'hwclouds\.com'),
        self.matchContent(r'hws_security@')
    ]
    if any(i for i in schemes):
        return True
    return False