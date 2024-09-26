#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CrawlProtect (Jean-Denis Brun)'


def is_waf(self):
    if self.matchCookie(r'^crawlprotecttag='):
        return True

    if self.matchContent(r'<title>crawlprotect'):
        return True

    if self.matchContent(r'this site is protected by crawlprotect'):
        return True

    return False
