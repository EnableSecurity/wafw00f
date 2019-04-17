#!/usr/bin/env python


NAME = 'BIG-IP Local Traffic Manager (F5 Networks)'


def is_waf(self):
    if self.matchcookie('^BIGipServer'):
        return True
    elif self.matchheader(('X-Cnection', '^close$'), attack=True):
        return True
    else:
        return False