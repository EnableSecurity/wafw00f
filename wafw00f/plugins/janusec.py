#!/usr/bin/env python


NAME = 'Janusec Application Gateway (Janusec)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Sites without modified block page return all fingerprints, so checking for any one of them works.
        if b'by Janusec Application Gateway' in page:
            return True
    return False