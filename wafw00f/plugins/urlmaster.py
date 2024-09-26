#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'URLMaster SecurityCheck (iFinity/DotNetNuke)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchHeader(('X-UrlMaster-Debug', '.+')):
        return True

    if self.matchHeader(('X-UrlMaster-Ex', '.+')):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r"Ur[li]RewriteModule"):
        return False

    if not self.matchContent(r'SecurityCheck'):
        return False

    return True
