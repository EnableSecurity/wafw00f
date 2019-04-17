#!/usr/bin/env python


NAME = 'Squarespace (Squarespace)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'BRICK-50' in page:
            return True
    return False