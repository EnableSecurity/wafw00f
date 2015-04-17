#!/usr/bin/env python


NAME = 'InfoGuard Airlock'


def is_waf(self):
    # credit goes to W3AF
    return self.matchcookie('^AL[_-]?(SESS|LB)=')
