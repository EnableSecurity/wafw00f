#!/usr/bin/env python


NAME = 'BIG-IP Application Security Manager (F5 Networks)'


def is_waf(self):
    # Actual fingerprint is this arising due to attack strings
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'The requested URL was rejected. Please consult with your administrator' in page:
            return True
    return False