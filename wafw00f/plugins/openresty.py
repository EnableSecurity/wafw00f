#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Open-Resty Lua Nginx (FLOSS)'


def is_waf(self):
    schema1 = [
        self.matchHeader(('Server', r'^openresty/[0-9\.]+?')),
        self.matchStatus(403)
    ]
    schema2 = [
        self.matchContent(r'openresty/[0-9\.]+?'),
        self.matchStatus(406)
    ]
    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False