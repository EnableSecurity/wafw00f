#!/usr/bin/env python


NAME = 'DotDefender (Applicure Technologies)'


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
        if any(i in responsepage for i in (b'dotDefender Blocked Your Request', 
            b'Applicure is the leading provider of web application security')):
            return True
    return False