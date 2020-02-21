#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sabre Firewall (Sabre)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'dxsupport\.sabre\.com')
    ]
    schema2 = [
        self.matchContent(r'<title>Application Firewall Error'),
        self.matchContent(r'add some important details to the email for us to investigate')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False