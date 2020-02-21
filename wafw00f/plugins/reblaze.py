#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Reblaze (Reblaze)'


def is_waf(self):
    schema1 = [
        self.matchCookie(r'^rbzid'),
        self.matchHeader(('Server', 'Reblaze Secure Web Gateway'))
    ]
    schema2 = [
        self.matchContent(r'current session has been terminated'),
        self.matchContent(r'do not hesitate to contact us'),
        self.matchContent(r'access denied \(\d{3}\)')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False