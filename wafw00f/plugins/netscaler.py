#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NetScaler AppFirewall (Citrix Systems)'


def is_waf(self):
    # This header can be obtained without attack mode
    if self.matchHeader(('Via', r'NS\-CACHE')):
        return True

    # Cookies are set only when someone is authenticated.
    # Not much reliable since wafw00f isn't authenticating.
    if self.matchCookie(r'^(ns_af=|citrix_ns_id|NSC_)'):
        return True

    if self.matchContent(r'(NS Transaction|AppFW Session) id'):
        return True

    if self.matchContent(r'Violation Category.{0,5}?APPFW_'):
        return True

    if self.matchContent(r'Citrix\|NetScaler'):
        return True

    # Reliable but not all servers return this header
    if self.matchHeader(('Cneonction', r'^(keep alive|close)'), attack=True):
        return True

    if self.matchHeader(('nnCoection', r'^(keep alive|close)'), attack=True):
        return True

    return False
