#!/usr/bin/env python


NAME = 'NinjaFirewall (NinTechNet)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Sites without modified block page return both, so checking for all
        # of them works.
        if all(i in page for i in (b'For security reasons, it was blocked and logged',
            b'<title>NinjaFirewall: 403 Forbidden')):
            return True
    return False