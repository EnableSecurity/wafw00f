#!/usr/bin/env python


NAME = 'Applicure dotDefender'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsepage = r
        if response.getheader('X-dotDefender-denied'):
            return True
        # Using a bytes like object directly for comparison resolved 
        # the load of decoding it again.
        if b'dotDefender Blocked Your Request' in responsepage:
            return True
    return False