#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NetScaler AppFirewall (Citrix Systems)'


def is_waf(self):
    schemes = [
        # This header can be obtained without attack mode
        self.matchHeader(('Via', r'NS\-CACHE')),
        # Cookies are set only when someone is authenticated.
        # Not much reliable since wafw00f isn't authenticating.
        self.matchCookie(r'^(ns_af=|citrix_ns_id|NSC_)'),
        self.matchContent(r'(NS Transaction|AppFW Session) id'),
        self.matchContent(r'Violation Category.{0,5}?APPFW_'),
        self.matchContent(r'Citrix\|NetScaler'),
        # Reliable but not all servers return this header
        self.matchHeader(('Cneonction', r'^(keep alive|close)'), attack=True),
        self.matchHeader(('nnCoection', r'^(keep alive|close)'), attack=True)
    ]
    if any(i for i in schemes):
        return True
    return False