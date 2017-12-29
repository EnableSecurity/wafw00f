#!/usr/bin/env python

NAME = 'Naxsi'

def is_waf(self):
    return self.matchheader(('X-Data-Origin', '^naxsi'))
