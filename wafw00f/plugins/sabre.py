#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sabre Firewall (Sabre)'


def is_waf(self):
    if self.matchContent(r'dxsupport\.sabre\.com'):
        return True

    if check_schema_01(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchContent(r'<title>Application Firewall Error'):
        return False

    if not self.matchContent(r'add some important details to the email for us to investigate'):
        return False

    return True
