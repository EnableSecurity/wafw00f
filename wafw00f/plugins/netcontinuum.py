#!/usr/bin/env python


NAME = 'NetContinuum'


def is_waf(self):
    return self.matchcookie('^NCI__SessionId=')
