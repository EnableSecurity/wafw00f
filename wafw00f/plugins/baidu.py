#!/usr/bin/env python

NAME = 'Yunjiasu (Baidu Cloud Computing)'

def is_waf(self):
    # There are some servers which return 'Server: Yunjiasu-nginx'
    if self.matchheader(('Server', r'Yunjiasu(.*)?')):
        return True
    return False