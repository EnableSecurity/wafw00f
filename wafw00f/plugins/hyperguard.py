#!/usr/bin/env python


NAME = 'HyperGuard (Art of Defense)'


def is_waf(self):
    if self.matchcookie('^WODSESSION='):
        return True
    return False