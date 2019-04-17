#!/usr/bin/env python


NAME = 'RSFirewall (RSJoomla!)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'COM_RSFIREWALL_403_FORBIDDEN', b'COM_RSFIREWALL_EVENT')):
            return True
    return False