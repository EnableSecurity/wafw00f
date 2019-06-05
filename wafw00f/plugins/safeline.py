#!/usr/bin/env python


NAME = 'Safeline (Chaitin Tech.)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        if any(i in responsepage for i in (b'SafeLine', b'<!-- event_id:')):
            return True
    return False