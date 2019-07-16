#!/usr/bin/env python


NAME = 'Incapsula (Imperva Inc.)'


def is_waf(self):
    if self.matchcookie(r'^incap_ses.*='):
        return True
    if self.matchcookie(r'^visid_incap.*='):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        if any(a in responsepage for a in (b"Incapsula incident ID:", b"/_Incapsula_Resource")):
            return True
    return False