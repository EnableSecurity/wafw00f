#!/usr/bin/env python

NAME = 'Wallarm'

def is_waf(self):
    return self.matchheader(('server', "nginx-wallarm"))

