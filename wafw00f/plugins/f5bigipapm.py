#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AP Manager (F5 Networks)'


def is_waf(self):
    schema1 = [
        self.matchCookie('^LastMRH_Session'),
        self.matchCookie('^MRHSession')
    ]
    schema2 = [
        self.matchCookie('^MRHSession'),
        self.matchHeader(('Server', r'Big([-_])?IP'), attack=True)
    ]
    schema3 = [
        self.matchCookie('^F5_fullWT'),
        self.matchCookie('^F5_fullWT'),
        self.matchCookie('^F5_HT_shrinked')
    ]
    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    if any(i for i in schema3):
        return True
    return False