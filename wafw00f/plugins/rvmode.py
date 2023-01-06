#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'RequestValidationMode (Microsoft)'


def is_waf(self):
    if self.matchContent(r'Request Validation has detected a potentially dangerous client input'):
        return True

    if self.matchContent(r'ASP\.NET has detected data in the request'):
        return True

    if self.matchContent(r'HttpRequestValidationException'):
        return True

    return False
