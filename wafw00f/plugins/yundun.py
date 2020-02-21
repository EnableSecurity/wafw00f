#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yundun (Yundun)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'YUNDUN')),
        self.matchHeader(('X-Cache', 'YUNDUN')),
        self.matchCookie(r'^yd_cookie='),
        self.matchContent(r'Blocked by YUNDUN Cloud WAF'),
        self.matchContent(r'yundun\.com/yd[-_]http[_-]error/'),
        self.matchContent(r'www\.yundun\.com/(static/js/fingerprint\d{1}?\.js)?')
    ]
    if any(i for i in schemes):
        return True
    return False