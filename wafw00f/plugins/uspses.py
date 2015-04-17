#!/usr/bin/env python


NAME = 'USP Secure Entry Server'


def is_waf(self):
    if self.matchheader(('server', 'Secure Entry Server')):
        return True
    return False
