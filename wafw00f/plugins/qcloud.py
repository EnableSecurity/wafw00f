#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Qcloud (Tencent Cloud)'


def is_waf(self):
    if not self.matchContent(r'腾讯云Web应用防火墙'):
        return False

    if not self.matchStatus(403):
        return False

    return True
