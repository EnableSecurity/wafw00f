#!/usr/bin/env python


NAME = 'Mission Control Application Shield (Mission Control)'


def is_waf(self):
    if self.matchheader(('server', 'Mission Control Application Shield')):
        return True
    return False