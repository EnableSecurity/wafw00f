#!/usr/bin/env python


NAME = 'Comodo'


def is_waf(self):
    if self.matchheader(('server', "Protected by COMODO WAF")):
        return True
