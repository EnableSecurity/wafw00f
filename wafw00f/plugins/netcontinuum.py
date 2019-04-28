#!/usr/bin/env python


NAME = 'NetContinuum (Barracuda Networks)'


def is_waf(self):
    if self.matchcookie(r'^NCI__SessionId='):
        return True
    return False