#!/usr/bin/env python
'''
Copyright (C) 2023, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiGate (Fortinet)'

def is_waf(self):
    if check_schema(self):
        return True

    return False


def check_schema(self):
    if not self.matchContent('Web Application Firewall'):
        return False

    if not self.matchContent('Event ID'):
        return False

    if not self.matchContent('globalurl.fortinet.net:8010'):
        return False

    return True
