#!/usr/bin/env python


NAME = 'Mission Control Application Shield'


def is_waf(self):
    if self.matchheader(('server', 'Mission Control Application Shield')):
        return True
    return False
