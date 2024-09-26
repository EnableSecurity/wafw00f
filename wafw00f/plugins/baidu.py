#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yunjiasu (Baidu Cloud Computing)'


def is_waf(self):
    if self.matchHeader(('Server', r'yunjiasu.*')):
        return True

    if self.matchContent(r'href="/.well-known/yunjiasu-cgi/'):
        return True

    if self.matchContent(r"document.cookie='yjs_use_ob=0"):
        return True

    return False
