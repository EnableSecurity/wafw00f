#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'YXLink (YxLink Technologies)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^yx_ci_session='),
        self.matchCookie(r'^yx_language='),
        self.matchHeader(('Server', r'Yxlink([\-_]?WAF)?'))
    ]
    if any(i for i in schemes):
        return True
    return False