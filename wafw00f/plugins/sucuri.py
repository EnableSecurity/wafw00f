#!/usr/bin/env python

NAME = 'Sucuri WAF'

def is_waf(self):
    return self.matchheader(('X-Sucuri-ID', '.+'))
