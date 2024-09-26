#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Malcare (Inactiv)'


def is_waf(self):
    if self.matchContent(r'firewall.{0,15}?powered.by.{0,15}?malcare.{0,15}?pro'):
        return True

    if self.matchContent('blocked because of malicious activities'):
        return True

    return False
