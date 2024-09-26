#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'pkSecurity IDS (pkSec)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchContent(r'pk.?Security.?Module'):
        return True

    if self.matchContent(r'Security.Alert'):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r'As this could be a potential hack attack'):
        return False

    if not self.matchContent(r'A safety critical (call|request) was (detected|discovered) and blocked'):
        return False

    if not self.matchContent(r'maximum number of reloads per minute and prevented access'):
        return False

    return True
