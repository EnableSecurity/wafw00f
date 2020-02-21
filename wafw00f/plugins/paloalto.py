#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers 
See the LICENSE file for copying permission.
'''

NAME = 'Palo Alto Next Gen Firewall (Palo Alto Networks)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Download of virus.spyware blocked'),
        self.matchContent(r'Palo Alto Next Generation Security Platform')
    ]
    if any(i for i in schemes):
        return True
    return False