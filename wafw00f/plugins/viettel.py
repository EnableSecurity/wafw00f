#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Viettel (Cloudrity)'


def is_waf(self):
    if self.matchContent(r"Access Denied.{0,10}?Viettel WAF"):
        return True

    if self.matchContent(r"cloudrity\.com\.(vn)?/"):
        return True

    if self.matchContent(r"Viettel WAF System"):
        return True

    return False
