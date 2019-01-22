#!/usr/bin/env python


NAME = 'Ergon Airlock'


def is_waf(self):
    # credit goes to W3AF
    return self.matchcookie('^AL[_-]?(SESS|LB)=')
