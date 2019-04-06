#!/usr/bin/env python


NAME = 'CDNNS Application Gateway'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'CdnNsWAF Application Gateway' in page:
            return True
    return False