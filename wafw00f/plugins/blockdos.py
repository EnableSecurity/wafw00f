#!/usr/bin/env python

NAME = 'BlockDoS'

def is_waf(self):
    return self.matchheader(('server', "BlockDos\.net"))

