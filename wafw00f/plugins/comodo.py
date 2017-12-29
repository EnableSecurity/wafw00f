#!/usr/bin/env python

NAME = 'Comodo WAF'

def is_waf(self):
    return self.matchheader(('server', "Protected by COMODO WAF"))

