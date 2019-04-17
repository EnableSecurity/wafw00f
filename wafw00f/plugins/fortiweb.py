#!/usr/bin/env python

NAME = 'FortiWeb (Fortinet)'

def is_waf(self):
    if self.matchcookie(r'^FORTIWAFSID='):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        # Found a site running a tweaked version of Fortiweb block page. Picked those only
        # in common. Discarded others.
        if all(m in responsepage for m in (b'fgd_icon', b'Web Page Blocked', b'URL:', b'Attack ID', 
            b'Message ID', b'Client IP')):
            return True
    return False