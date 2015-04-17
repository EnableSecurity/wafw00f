#!/usr/bin/env python


NAME = 'NetContinuum'


def is_waf(self):
    # credit goes to W3AF
    return self.matchcookie('^NCI__SessionId=')
