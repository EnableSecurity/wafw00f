#!/usr/bin/env python


NAME = 'PowerCDN'


def is_waf(self):
    if self.matchheader(('PowerCDN', '.+')):
        return True
    return False