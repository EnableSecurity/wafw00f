#!/usr/bin/env python


NAME = 'DataPower (IBM)'


def is_waf(self):
    if self.matchheader(('X-Backside-Transport', r'^(OK|FAIL)')):
        return True
    return False