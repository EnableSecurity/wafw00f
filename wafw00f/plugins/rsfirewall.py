#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'RSFirewall (RSJoomla!)'


def is_waf(self):
    if self.matchContent(r'com_rsfirewall_(\d{3}_forbidden|event)?'):
        return True

    return False
