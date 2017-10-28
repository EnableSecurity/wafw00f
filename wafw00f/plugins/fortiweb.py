#!/usr/bin/env python


NAME = 'Fortiweb'


def is_waf(self):
    if self.matchcookie('\AFORTIWAFSID='):
        return True
