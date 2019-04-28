#!/usr/bin/env python


NAME = 'Teros (Citrix Systems)'


def is_waf(self):
    if self.matchcookie(r'^st8id='):
        return True
    return False