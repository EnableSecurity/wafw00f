#!/usr/bin/env python


NAME = 'Teros WAF'


def is_waf(self):
    if self.matchcookie('^st8id='):
        return True
    return False