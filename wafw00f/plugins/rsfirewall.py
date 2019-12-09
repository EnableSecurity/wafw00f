#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'RSFirewall (RSJoomla!)'


def is_waf(self):
    schemes = [
        self.matchContent(r'com_rsfirewall_(\d{3}_forbidden|event)?')
    ]
    if any(i for i in schemes):
        return True
    return False