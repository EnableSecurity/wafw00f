#!/usr/bin/env python


NAME = 'Armor Defense (Armor)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Armor reveals itself only in blockpage twice.
        if any(i in page for i in (b'blocked by website protection from Armor', 
            b'please create an Armor support ticket')):
            return True
    return False