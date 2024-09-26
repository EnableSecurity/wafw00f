#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Instart DX (Instart Logic)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchHeader(('X-Instart-Request-ID', '.+')):
        return True

    if self.matchHeader(('X-Instart-Cache', '.+')):
        return True

    if self.matchHeader(('X-Instart-WL', '.+')):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r'the requested url was rejected'):
        return False

    if not self.matchContent(r'please consult with your administrator'):
        return False

    if not self.matchContent(r'your support id is'):
        return False

    return True
