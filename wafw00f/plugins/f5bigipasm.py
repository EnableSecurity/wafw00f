#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AppSec Manager (F5 Networks)'


def is_waf(self):
    if check_schema_01(self):
        return True

    # ASM ≥ 11.4.0 → eight hex digits after “TS” - https://my.f5.com/manage/s/article/K6850
    if self.matchCookie(r'TS[a-fA-F0-9]{8}=.+'):
        return True
    
    # ASM 10.0.0 – 11.3.0 → six hex digits after “TS” - https://my.f5.com/manage/s/article/K6850
    if self.matchCookie(r'TS[a-fA-F0-9]{6}=.+'):
        return True

    return False


def check_schema_01(self):
    if not self.matchContent('the requested url was rejected'):
        return False

    if not self.matchContent('please consult with your administrator'):
        return False

    return True
