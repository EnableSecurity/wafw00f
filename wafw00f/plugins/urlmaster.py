#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'URLMaster SecurityCheck (iFinity/DotNetNuke)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-UrlMaster-Debug', '.+')),
        self.matchHeader(('X-UrlMaster-Ex', '.+')),
        self.matchContent(r"UrilRewriteModule"),
        self.matchContent(r'SecurityCheck')
    ]
    if any(i for i in schemes):
        return True
    return False