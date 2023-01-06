#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'RayWAF (WebRay Solutions)'


def is_waf(self):
    if self.matchHeader(('Server', r'WebRay\-WAF')):
        return True

    if self.matchHeader(('DrivedBy', r'RaySrv.RayEng/[0-9\.]+?')):
        return True

    return False
