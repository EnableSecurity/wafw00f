#!/usr/bin/env python


NAME = 'ChinaCache CDN Load Balancer'


def is_waf(self):
    if self.matchheader(('Powered-By-ChinaCache', '.+')):
        return True
    return False