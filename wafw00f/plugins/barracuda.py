#!/usr/bin/env python


NAME = 'Barracuda Application Firewall (Barracuda Networks)'


def is_waf(self):
    if self.matchcookie(r'^barra_counter_session='):
        return True
    if self.matchcookie(r'^BNI__BARRACUDA_LB_COOKIE='):
        return True
    if self.matchcookie(r'^BNI_persistence='):
        return True
    if self.matchcookie(r'^BN[IE]S_.*?='):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        # At the bottom of blockpage there is a copyright
        # notice indicating barracuda networks.
        if b'Barracuda Networks, Inc' in responsepage:
            return True
    return False