#!/usr/bin/env python


NAME = 'Shield Security (One Dollar Plugin)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsebody = r
        # Most reliable fingerprint is this on block page
        if any(i in responsebody for i in (b'You were blocked by the Shield', b'remaining transgression(s) against this site', b"Something in the URL, Form or Cookie data wasn't appropriate")):
            return True
    return False