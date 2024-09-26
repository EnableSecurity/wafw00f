#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wpmudev WAF (Incsub)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchContent(r'href="http(s)?.\/\/wpmudev.com\/.{0,15}?'):
        return False

    if not self.matchContent(r'Click on the Logs tab, then the WAF Log.'):
        return False

    if not self.matchContent(r'Choose your site from the list'):
        return False

    if not self.matchStatus(403):
        return False

    return True


def check_schema_02(self):
    if not self.matchContent(r'<h1>Whoops, this request has been blocked!'):
        return False

    if not self.matchContent(r'This request has been deemed suspicious'):
        return False

    if not self.matchContent(r'possible attack on our servers.'):
        return False

    if not self.matchStatus(403):
        return False

    return True
