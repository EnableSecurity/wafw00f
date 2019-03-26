#!/usr/bin/env python


NAME = 'Applicure dotDefender'


def is_waf(self):
    detected = False
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsepage = r
        # Using a bytes like object directly for comparison resolved 
        # the load of decoding it again.
        if b'dotDefender Blocked Your Request' in responsepage:
            detected = True
            break
    return detected
    return self.matchheader(['X-dotDefender-denied', '^1$'], attack=True)
