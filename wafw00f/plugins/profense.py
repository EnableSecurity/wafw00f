#!/usr/bin/env python


NAME = 'Profense'


def is_waf(self):
    if self.matchheader(('server', 'profense')):
        return True
    if self.matchcookie('^PLBSID='):
        return True
    return False