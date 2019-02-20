#!/usr/bin/env python


NAME = 'Mission Control Application Shield'


def is_waf(self):
    return self.matchheader(('server', 'Mission Control Application Shield'))
