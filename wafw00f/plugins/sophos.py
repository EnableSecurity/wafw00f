#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'UTM Web Protection (Sophos)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'www\.sophos\.com'),
        self.matchContent(r'Powered by.?(Sophos)? UTM Web Protection')
    ]
    schema2 = [
        self.matchContent(r'<title>Access to the requested URL was blocked'),
        self.matchContent(r'Access to the requested URL was blocked'),
        self.matchContent(r'incident was logged with the following log identifier'),
        self.matchContent(r'Inbound Anomaly Score exceeded'),
        self.matchContent(r'Your cache administrator is')
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False