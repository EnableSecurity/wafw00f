#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FirePass (F5 Networks)'


def is_waf(self):
    schema1 = [
        self.matchCookie('^VHOST'),
        self.matchHeader(('Location', r'\/my\.logon\.php3'))
    ]
    schema2 = [
        self.matchCookie(r'^F5_fire.+?'),
        self.matchCookie('^F5_passid_shrinked')
    ]
    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False