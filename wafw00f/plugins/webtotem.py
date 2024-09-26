#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebTotem (WebTotem)'


def is_waf(self):
    if self.matchContent(r"The current request was blocked.{0,8}?>WebTotem"):
        return True

    return False
