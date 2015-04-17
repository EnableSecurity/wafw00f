#!/usr/bin/env python


NAME = 'F5 BIG-IP LTM'


def is_waf(self):
    detected = False
    if self.matchcookie('^BIGipServer'):
        return True
    elif self.matchheader(('X-Cnection', '^close$'), attack=True):
        return True
    else:
        return False
