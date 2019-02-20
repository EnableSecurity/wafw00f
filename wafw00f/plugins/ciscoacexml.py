#!/usr/bin/env python


NAME = 'Cisco ACE XML Gateway'


def is_waf(self):
    return self.matchheader(('server', 'ACE XML Gateway'))
