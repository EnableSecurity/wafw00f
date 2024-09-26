#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AP Manager (F5 Networks)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    if check_schema_03(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchCookie('^LastMRH_Session'):
        return False

    if not self.matchCookie('^MRHSession'):
        return False

    return True


def check_schema_02(self):
    if not self.matchCookie('^MRHSession'):
        return False

    if not self.matchHeader(('Server', r'Big([-_])?IP'), attack=True):
        return False

    return True


def check_schema_03(self):
    if self.matchCookie('^F5_fullWT'):
        return True

    if self.matchCookie('^F5_fullWT'):
        return True

    if self.matchCookie('^F5_HT_shrinked'):
        return True

    return False
