#!/usr/bin/env python

NAME = 'BlockDoS'

def is_waf(self):
    if self.matchheader(('server', "BlockDos\\.net")):
        return True
    return False