#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FirePass (F5 Networks)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchCookie('^VHOST'):
        return False

    if not self.matchHeader(('Location', r'\/my\.logon\.php3')):
        return False

    return True


def check_schema_02(self):
    if not self.matchCookie(r'^F5_fire.+?'):
        return False

    if not self.matchCookie('^F5_passid_shrinked'):
        return False

    return True
