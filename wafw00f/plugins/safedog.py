#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Safedog (SafeDog)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^safedog\-flow\-item='),

        # there are actually two signatures for Safedog
        # and both Server and X-Powered-By should be checked
        self.matchHeader(('Server', 'Safedog')),
        self.matchHeader(('Server', 'WAF/2\.0')),
        self.matchHeader(('X-Powered-By', 'WAF/2\.0')),
        self.matchHeader(('X-Powered-By', 'Safedog')),

        self.matchContent(r'safedogsite/broswer_logo\.jpg'),
        self.matchContent(r'404\.safedog\.cn/sitedog_stat.html'),
        self.matchContent(r'404\.safedog\.cn/images/safedogsite/head\.png')
    ]
    if any(i for i in schemes):
        return True
    return False