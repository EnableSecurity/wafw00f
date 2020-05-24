#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wpmudev WAF (Incsub)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Log in to the <a href="https://wpmudev.com/hub/hosting/" rel="noreferrer">Hosting Hub</a>'),
        self.matchContent(r'Choose your site from the list'),
        self.matchContent(r'Click on the Logs tab, then the WAF Log.'),
        self.matchStatus(403)
    ]
    if all(i for i in schemes):
        return True
    return False