#!/usr/bin/env python3
'''
Copyright (C) 2023, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiGate (Fortinet)'

def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False

def check_schema_01(self):
    if not self.matchContent('//globalurl.fortinet.net'):
        return False

    if not self.matchContent('FortiGate Application Control'):
        return False

    return True

def check_schema_02(self):
    if not self.matchContent('Web Application Firewall'):
        return False

    if not self.matchContent('Event ID'):
        return False

    if not self.matchContent('//globalurl.fortinet.net'):
        return False

    return True
