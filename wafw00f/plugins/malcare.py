#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Malcare (Inactiv)'


def is_waf(self):
    schemes = [
        self.matchContent(r'firewall.+?powered.by.+?malcare.+?pro'),
        self.matchContent('blocked because of malicious activities')
    ]
    if any(i for i in schemes):
        return True
    return False