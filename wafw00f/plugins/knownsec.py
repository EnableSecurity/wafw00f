#!/usr/bin/env python


NAME = 'KS-WAF (KnownSec)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'/ks-waf-error.png' in page:
            return True
    return False