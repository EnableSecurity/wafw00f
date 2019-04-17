#!/usr/bin/env python


NAME = 'HyperGuard (Art of Defense)'


def is_waf(self):
    if self.matchcookie(r'^WODSESSION='):
        return True
    return False