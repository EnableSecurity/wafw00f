#!/usr/bin/env python


NAME = 'Safedog'


def is_waf(self):
    if self.matchcookie('^safedog-flow-item='):
        return True
    if self.matchheader(('server', '^Safedog')):
        return True
    if self.matchheader(('x-powered-by', '^WAF/\d\.\d')):
        return True
    return False
