#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebTotem (WebTotem)'


def is_waf(self):
    schemes = [
        self.matchContent(r"The current request was blocked.{0,8}?>WebTotem")
    ]
    if any(i for i in schemes):
        return True
    return False