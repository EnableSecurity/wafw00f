#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yundun (Yundun)'


def is_waf(self):
    if self.matchHeader(('Server', 'YUNDUN')):
        return True

    if self.matchHeader(('X-Cache', 'YUNDUN')):
        return True

    if self.matchCookie(r'^yd_cookie='):
        return True

    if self.matchContent(r'Blocked by YUNDUN Cloud WAF'):
        return True

    if self.matchContent(r'yundun\.com/yd[-_]http[_-]error/'):
        return True

    if self.matchContent(r'www\.yundun\.com/(static/js/fingerprint\d{1}?\.js)?'):
        return True

    return False
