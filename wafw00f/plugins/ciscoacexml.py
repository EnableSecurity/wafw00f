#!/usr/bin/env python


NAME = 'Cisco ACE XML Gateway'


def is_waf(self):
    if self.matchheader(('server', 'ACE XML Gateway')):
        return True
    return False
