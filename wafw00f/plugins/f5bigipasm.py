#!/usr/bin/env python


NAME = 'F5 BIG-IP ASM'


def is_waf(self):
    if self.matchcookie('^TS[a-zA-Z0-9]{3,8}='):
        return True
    return False