#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = '360WangZhanBao (360 Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'qianxin\-waf')),
        self.matchHeader(('WZWS-Ray', r'(.+)?')),
        self.matchHeader(('X-Powered-By-360WZB', r'.+?')),
        self.matchHeader(('X-Safe-Firewall', r'(zhuji.)?360.cn.[0-9\.]+?(.[A-Z0-9]+)?')),
        self.matchContent(r'wzws\-waf\-cgi/'),
        self.matchContent(r'wangshan\.360\.cn'),
        self.matchStatus(493)
    ]
    if any(i for i in schemes):
        return True
    return False