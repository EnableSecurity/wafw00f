#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sucuri CloudProxy (Sucuri Inc.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Sucuri-ID', r'.+?')),
        self.matchHeader(('X-Sucuri-Cache', r'.+?')),
        self.matchHeader(('Server', r'Sucuri(\-Cloudproxy)?')),
        self.matchHeader(('X-Sucuri-Block', r'.+?'), attack=True),
        self.matchContent(r"Access Denied.{0,6}?Sucuri Website Firewall"),
        self.matchContent(r"<title>Sucuri WebSite Firewall.{0,6}?(CloudProxy)?.{0,6}?Access Denied"),
        self.matchContent(r"sucuri\.net/privacy\-policy"),
        self.matchContent(r"cdn\.sucuri\.net/sucuri[-_]firewall[-_]block\.css"),
        self.matchContent(r'cloudproxy@sucuri\.net')
    ]
    if any(i for i in schemes):
        return True
    return False