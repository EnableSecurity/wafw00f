#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Open-Resty Lua Nginx (FLOSS)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchHeader(('Server', r'^openresty/[0-9\.]+?')):
        return False

    if not self.matchStatus(403):
        return False

    return True


def check_schema_02(self):
    if not self.matchContent(r'openresty/[0-9\.]+?'):
        return False

    if not self.matchStatus(406):
        return False

    return True
