#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Astra (Czar Securities)'


def is_waf(self):
    if self.matchCookie(r'^cz_astra_csrf_cookie'):
        return True

    if self.matchContent(r'astrawebsecurity\.freshdesk\.com'):
        return True

    if self.matchContent(r'www\.getastra\.com/assets/images'):
        return True

    return False
