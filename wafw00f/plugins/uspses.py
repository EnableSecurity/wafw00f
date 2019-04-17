#!/usr/bin/env python


NAME = 'Secure Entry Server (USP)'


def is_waf(self):
    if self.matchheader(('server', 'Secure Entry Server')):
        return True
    return False
