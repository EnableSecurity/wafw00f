#!/usr/bin/env python


NAME = 'NSFocus (NSFocus Global Inc.)'


def is_waf(self):
    if self.matchheader(('server', 'NSFocus')):
        return True
    return False