#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AliYunDun (Alibaba Cloud Computing)'


def is_waf(self):
    if not self.matchContent(r'error(s)?\.aliyun(dun)?\.(com|net)?'):
        return False

    if not self.matchContent(r'alicdn\.com\/sd\-base\/static\/\d{1,2}\.\d{1,2}\.\d{1,2}\/image\/405\.png'):
        return False

    if not self.matchContent(r'Sorry, your request has been blocked as it may cause potential threats to the server\'s security.'):
        return False

    if not self.matchStatus(405):
        return False

    return True
