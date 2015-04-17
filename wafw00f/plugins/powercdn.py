#!/usr/bin/env python


NAME = 'PowerCDN'


def is_waf(self):
    return self.matchheader(('PowerCDN', '.+'))
