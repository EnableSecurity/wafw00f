#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'URLMaster SecurityCheck (iFinity/DotNetNuke)'


def is_waf(self):
    schema1 = [
        self.matchHeader(('X-UrlMaster-Debug', '.+')),
        self.matchHeader(('X-UrlMaster-Ex', '.+')),
    ]
    schema2 = [
        self.matchContent(r"Ur[li]RewriteModule"),
        self.matchContent(r'SecurityCheck')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False