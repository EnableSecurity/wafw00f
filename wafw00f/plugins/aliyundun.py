#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AliYunDun (Alibaba Cloud Computing)'


def is_waf(self):
    if not self.matchContent(r'error(s)?\.aliyun(dun)?\.(com|net)?'):
        return False

    if not self.matchCookie(r'^aliyungf_tc='):
        return False

    if not self.matchContent(r'cdn\.aliyun(cs)?\.com'):
        return False

    if not self.matchStatus(405):
        return False

    return True
