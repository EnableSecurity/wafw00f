#!/usr/bin/env python


NAME = 'BIG-IP Application Security Manager (F5 Networks)'


def is_waf(self):
    if self.matchcookie('^TS[a-zA-Z0-9]{3,8}='):
        return True
    return False