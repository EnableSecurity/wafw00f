#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = '360WangZhanBao (360 Technologies)'


def is_waf(self):
    if self.matchHeader(('Server', r'qianxin\-waf')):
        return True

    if self.matchHeader(('WZWS-Ray', r'.+?')):
        return True

    if self.matchHeader(('X-Powered-By-360WZB', r'.+?')):
        return True

    if self.matchContent(r'wzws\-waf\-cgi/'):
        return True

    if self.matchContent(r'wangshan\.360\.cn'):
        return True

    if self.matchStatus(493):
        return True

    return False
