#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'UTM Web Protection (Sophos)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchContent(r'www\.sophos\.com'):
        return True

    if self.matchContent(r'Powered by.?(Sophos)? UTM Web Protection'):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r'<title>Access to the requested URL was blocked'):
        return False

    if not self.matchContent(r'Access to the requested URL was blocked'):
        return False

    if not self.matchContent(r'incident was logged with the following log identifier'):
        return False

    if not self.matchContent(r'Inbound Anomaly Score exceeded'):
        return False

    if not self.matchContent(r'Your cache administrator is'):
        return False

    return True
