#!/usr/bin/env python3
'''
Copyright (C) 2021, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Shieldon Firewall (Shieldon.io)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    if check_schema_03(self):
        return True

    if self.matchHeader((r'[Xx]-[Pp]rotected-[Bb]y', 'shieldon.io')):
        return True

    return False


def check_schema_01(self):
    if not self.matchContent('Please solve CAPTCHA'):
        return False

    if not self.matchContent('shieldon_captcha'):
        return False

    if not self.matchContent('Unusual behavior detected'):
        return False

    if not self.matchContent('status-user-info'):
        return False

    return True


def check_schema_02(self):
    if not self.matchContent('Access denied'):
        return False

    if not self.matchContent('The IP address you are using has been blocked.'):
        return False

    if not self.matchContent('status-user-info'):
        return False

    return True


def check_schema_03(self):
    if not self.matchContent('Please line up'):
        return False

    if not self.matchContent('This page is limiting the number of people online. Please wait a moment.'):
        return False

    return True
