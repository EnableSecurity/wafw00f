#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sucuri CloudProxy (Sucuri Inc.)'


def is_waf(self):
    if self.matchHeader(('X-Sucuri-ID', r'.+?')):
        return True

    if self.matchHeader(('X-Sucuri-Cache', r'.+?')):
        return True

    if self.matchHeader(('Server', r'Sucuri(\-Cloudproxy)?')):
        return True

    if self.matchHeader(('X-Sucuri-Block', r'.+?'), attack=True):
        return True

    if self.matchContent(r"Access Denied.{0,6}?Sucuri Website Firewall"):
        return True

    if self.matchContent(r"<title>Sucuri WebSite Firewall.{0,6}?(CloudProxy)?.{0,6}?Access Denied"):
        return True

    if self.matchContent(r"sucuri\.net/privacy\-policy"):
        return True

    if self.matchContent(r"cdn\.sucuri\.net/sucuri[-_]firewall[-_]block\.css"):
        return True

    if self.matchContent(r'cloudproxy@sucuri\.net'):
        return True

    return False
