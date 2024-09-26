#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebKnight (AQTRONIX)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    if check_schema_03(self):
        return True

    return False


def check_schema_01(self):
    if not self.matchStatus(999):
        return False

    if not self.matchReason('No Hacking'):
        return False

    return True


def check_schema_02(self):
    if not self.matchStatus(404):
        return False

    if not self.matchReason('Hack Not Found'):
        return False

    return True


def check_schema_03(self):
    if self.matchContent(r'WebKnight Application Firewall Alert'):
        return True

    if self.matchContent(r'What is webknight\?'):
        return True

    if self.matchContent(r'AQTRONIX WebKnight is an application firewall'):
        return True

    if self.matchContent(r'WebKnight will take over and protect'):
        return True

    if self.matchContent(r'aqtronix\.com/WebKnight'):
        return True

    if self.matchContent(r'AQTRONIX.{0,10}?WebKnight'):
        return True

    return False
