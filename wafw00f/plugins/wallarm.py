#!/usr/bin/env python

NAME = 'Wallarm'

def is_waf(self):
    if self.matchheader(('server', "nginx-wallarm")):
        return True
    return False

