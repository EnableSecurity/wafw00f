#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Trafficshield (F5 Networks)'


def is_waf(self):
    if self.matchCookie('^ASINFO='):
        return True

    if self.matchHeader(('Server', 'F5-TrafficShield')):
        return True

    return False
