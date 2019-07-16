#!/usr/bin/env python


NAME = 'SiteGround (SiteGround)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'Our system thinks you might be a robot!', 
            b'The page you are trying to access is restricted due to a security rule')):
            return True
    return False