#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Expression Engine (EllisLab)'


def is_waf(self):
    schemes = [
        # I have seen some sites use a tracking header and sets a cookie upon authentication
        # 'Set-Cookie: _exp_tracking=rufyhweiuitefgcxyniercyft5-6dctuxeygfr'
        self.matchCookie(r'^exp_track.+?='),
        # There are traces found where cookie is returning values like:
        # Set-Cookie: exp_last_query=834y8d73y94d8g983u4shn8u4shr3uh3
        # Set-Cookie: exp_last_id=b342b432b1a876r8
        self.matchCookie(r'^exp_last_.+?=', attack=True),
        # In-page fingerprints vary a lot in different sites. Hence these are not quite reliable.
        self.matchContent(r'invalid get data')
    ]
    if any(i for i in schemes):
        return True
    return False