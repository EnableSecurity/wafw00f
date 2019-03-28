#!/usr/bin/env python


NAME = 'Art of Defence HyperGuard'


def is_waf(self):
    return self.matchcookie('^WODSESSION=')