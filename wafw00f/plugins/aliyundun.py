#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AliYunDun (Alibaba Cloud Computing)'


def is_waf(self):
    schemes = [
        self.matchContent(r'error(s)?\.aliyun(dun)?\.(com|net)?'),
        self.matchCookie(r'^aliyungf_tc='),
        self.matchContent(r'cdn\.aliyun(cs)?\.com'),
        self.matchStatus(405)
        ]
    if all(i for i in schemes):
        return True
    return False