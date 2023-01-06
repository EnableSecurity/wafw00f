#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'YXLink (YxLink Technologies)'


def is_waf(self):
    if self.matchCookie(r'^yx_ci_session='):
        return True

    if self.matchCookie(r'^yx_language='):
        return True

    if self.matchHeader(('Server', r'Yxlink([\-_]?WAF)?')):
        return True

    return False
