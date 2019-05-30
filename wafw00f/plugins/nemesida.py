#!/usr/bin/env python


NAME = 'Nemesida (PentestIt)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # The WAF requires the owner to create a inbox email ID with alias 'nwaf@site.com' for
        # reporting anomalies and bugs.
        if any(i in page for i in (b'Suspicious activity detected. Access to the site is blocked.',  
            b'nwaf@')):
            return True
    return False