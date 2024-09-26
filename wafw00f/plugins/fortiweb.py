#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiWeb (Fortinet)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchCookie(r'^FORTIWAFSID='):
        return True

    if self.matchContent('.fgd_icon'):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent('fgd_icon'):
        return False

    if not self.matchContent('web.page.blocked'):
        return False

    if not self.matchContent('url'):
        return False

    if not self.matchContent('attack.id'):
        return False

    if not self.matchContent('message.id'):
        return False

    if not self.matchContent('client.ip'):
        return False

    return True
