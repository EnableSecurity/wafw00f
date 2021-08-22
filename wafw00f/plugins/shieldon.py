#!/usr/bin/env python
'''
Copyright (C) 2021, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Shieldon Firewall (Shieldon.io)'


def is_waf(self):
    captcha = [
        self.matchContent('Please solve CAPTCHA'),
        self.matchContent('shieldon_captcha'),
        self.matchContent('Unusual behavior detected'),
        self.matchContent('status-user-info'),
    ]

    if all(i for i in captcha):
        return True

    ip_banned = [
        self.matchContent('Access denied'),
        self.matchContent('The IP address you are using has been blocked.'),
        self.matchContent('status-user-info'),
    ]

    if all(i for i in ip_banned):
        return True

    rate_limited = [
        self.matchContent('Please line up'),
        self.matchContent('This page is limiting the number of people online. Please wait a moment.'),
    ]

    if all(i for i in rate_limited):
        return True

    headers = [
        self.matchHeader((r'[Xx]-[Pp]rotected-[Bb]y', 'shieldon.io')),
    ]

    if any(i for i in headers):
        return True

    return False
