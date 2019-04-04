#!/usr/bin/env python


NAME = 'IBM DataPower'


def is_waf(self):
    if self.matchheader(('X-Backside-Transport', '^(OK|FAIL)')):
        return True
    return False