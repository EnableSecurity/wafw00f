#!/usr/bin/env python


NAME = 'Art of Defence HyperGuard'


def is_waf(self):
    if self.matchcookie('^WODSESSION='):
        return True
    return False