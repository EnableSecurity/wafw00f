#!/usr/bin/env python


NAME = 'NSFocus'


def is_waf(self):
    if self.matchheader(('server', 'NSFocus')):
        return True
    return False
