#!/usr/bin/env python


NAME = 'Teros WAF'


def is_waf(self):
    # credit goes to W3AF
    return self.matchcookie('^st8id=')
