#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiWeb (Fortinet)'


def is_waf(self):
    schema1 = [
        self.matchCookie(r'^FORTIWAFSID='),
        self.matchContent('.fgd_icon')
    ]
    schema2 = [
        self.matchContent('fgd_icon'),
        self.matchContent('web.page.blocked'),
        self.matchContent('url'),
        self.matchContent('attack.id'),
        self.matchContent('message.id'),
        self.matchContent('client.ip')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False