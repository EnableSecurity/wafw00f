#!/usr/bin/env python


NAME = 'GoDaddy Website Protection (GoDaddy)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Sites without modified block page return both, so checking for any one of them works.
        if any(i in page for i in (b'GoDaddy Security - Access Denied', b'Access Denied - GoDaddy Website Firewall')):
            return True
    return False