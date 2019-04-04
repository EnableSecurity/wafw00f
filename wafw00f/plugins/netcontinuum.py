#!/usr/bin/env python


NAME = 'NetContinuum'


def is_waf(self):
    if self.matchcookie('^NCI__SessionId='):
        return True
    return False