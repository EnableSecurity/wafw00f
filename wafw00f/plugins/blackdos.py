#!/usr/bin/env python


NAME = 'BlackDos'


def is_waf(self):
    if self.matchheader(('server', "BlockDos\.net")):
        return True
