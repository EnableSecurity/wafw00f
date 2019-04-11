#!/usr/bin/env python


NAME = 'Palo Alto'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if all(i in page for i in (b'Download of virus/spyware blocked', b'blocked in accordance with company policy')):
            return True
        if b'Palo Alto Next Generation Security Platform' in page:
            return True
    return False