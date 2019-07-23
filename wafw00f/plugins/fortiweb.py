#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiWeb (Fortinet)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^FORTIWAFSID='),
        self.matchContent('fgd_icon'),
        self.matchContent('web.page.blocked'),
        self.matchContent('url'),
        self.matchContent('attack.id'),
        self.matchContent('message.id'),
        self.matchContent('client.ip')
    ]
    if all(i for i in schemes):
        return True
    return False