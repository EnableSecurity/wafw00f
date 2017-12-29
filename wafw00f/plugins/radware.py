#!/usr/bin/env python

NAME = 'Radware AppWall'

def is_waf(self):
    return self.matchheader(('X-SL-CompState', '.'))
