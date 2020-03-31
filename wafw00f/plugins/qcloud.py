#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Qcloud (Tencent Cloud)'


def is_waf(self):
    schemes = [
        self.matchContent(r'腾讯云Web应用防火墙'),
        self.matchStatus(403)
        ]
    if all(i for i in schemes):
        return True
    return False
