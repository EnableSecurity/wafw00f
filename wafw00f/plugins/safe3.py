#!/usr/bin/env python


NAME = 'Safe3 Web Firewall (Safe3)'


def is_waf(self):
    # Safe3 exposes itself below the Forbidden Header
    if self.matchheader(('Server', 'Safe3 Web Firewall')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'Safe3waf/' in page:
            return True
    return False