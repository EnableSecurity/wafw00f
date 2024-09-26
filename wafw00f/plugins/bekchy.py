#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Bekchy (Faydata Technologies Inc.)'


def is_waf(self):
    # Both signatures are contained within response, so checking for any one of them
    # Sometimes I observed that there is an XHR request being being made to submit the
    # report data automatically upon page load. In those cases a missing https is causing
    # false negatives.
    if self.matchContent(r'Bekchy.{0,10}?Access Denied'):
        return True

    if self.matchContent(r'bekchy\.com/report'):
        return True

    return False
