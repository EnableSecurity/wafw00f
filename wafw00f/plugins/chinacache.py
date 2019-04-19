#!/usr/bin/env python


NAME = 'ChinaCache CDN Load Balancer (ChinaCache)'


def is_waf(self):
    if self.matchheader(('Powered-By-ChinaCache', '.+')):
        return True
    return False