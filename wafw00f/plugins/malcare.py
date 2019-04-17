#!/usr/bin/env python


NAME = 'Malcare (Inactiv)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'Firewall</h2><h3>powered by</h3><h2>MalCare - Pro', 
            b'Blocked because of Malicious Activities')):
            return True
    return False