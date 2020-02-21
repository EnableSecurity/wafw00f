#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Bekchy (Faydata Technologies Inc.)'


def is_waf(self):
    schemes = [
        # Both signatures are contained within response, so checking for any one of them
        # Sometimes I observed that there is an XHR request being being made to submit the 
        # report data automatically upon page load. In those cases a missing https is causing
        # false negatives.
        self.matchContent(r'Bekchy.{0,10}?Access Denied'),
        self.matchContent(r'bekchy\.com/report')
    ]
    if any(i for i in schemes):
        return True
    return False