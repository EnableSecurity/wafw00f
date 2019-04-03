#!/usr/bin/env python

NAME = 'FortiWeb'

def is_waf(self):
    if self.matchcookie('FORTIWAFSID='):
        return True
    elif self.matchcookie('cookiesession1='):
        return True
    else:
        return False
