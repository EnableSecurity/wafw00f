#!/usr/bin/env python


NAME = 'NetContinuum'


def is_waf(self):
    if self.matchcookie(r'^NCI__SessionId='):
        return True
    return False