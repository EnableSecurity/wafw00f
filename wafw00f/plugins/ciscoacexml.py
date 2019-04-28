#!/usr/bin/env python


NAME = 'ACE XML Gateway (Cisco)'


def is_waf(self):
    if self.matchheader(('server', 'ACE XML Gateway')):
        return True
    return False