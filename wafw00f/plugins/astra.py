#!/usr/bin/env python


NAME = 'Astra Web Protection (Czar Securities)'


def is_waf(self):
    if self.matchcookie(r'^cz_astra_csrf_cookie'):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        if b'www.getastra.com/assets/images' in responsepage:
            return True
    return False