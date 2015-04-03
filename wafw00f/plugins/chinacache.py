#!/usr/bin/env python


NAME = 'ChinaCache-CDN'


def is_waf(self):
    return self.matchheader(('Powered-By-ChinaCache', '.+'))
