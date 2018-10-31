#!/usr/bin/env python

NAME = 'AWS WAF'

def is_waf(self):
    return self.matchheader(('Server', 'awselb/2\\.0'), attack=True)
