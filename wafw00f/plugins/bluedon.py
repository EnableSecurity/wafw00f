#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Bluedon (Bluedon IST)'


def is_waf(self):
    # Found sample servers returning 'Server: BDWAF/2.0'
    if self.matchHeader(('Server', r'BDWAF')):
        return True

    if self.matchContent(r'bluedon web application firewall'):
        return True

    return False
