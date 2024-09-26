#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Expression Engine (EllisLab)'


def is_waf(self):
    # I have seen some sites use a tracking header and sets a cookie upon authentication
    # 'Set-Cookie: _exp_tracking=rufyhweiuitefgcxyniercyft5-6dctuxeygfr'
    if self.matchCookie(r'^exp_track.+?='):
        return True

    # There are traces found where cookie is returning values like:
    # Set-Cookie: exp_last_query=834y8d73y94d8g983u4shn8u4shr3uh3
    # Set-Cookie: exp_last_id=b342b432b1a876r8
    if self.matchCookie(r'^exp_last_.+?=', attack=True):
        return True

    # In-page fingerprints vary a lot in different sites. Hence these are not quite reliable.
    if self.matchContent(r'invalid get data'):
        return True

    return False
