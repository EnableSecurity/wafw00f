#!/usr/bin/env python

NAME = 'XLabs Security WAF'

def is_waf(self):
    return self.matchheader(('x-cdn', 'XLabs Security'))
