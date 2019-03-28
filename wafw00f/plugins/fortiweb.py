#!/usr/bin/env python

NAME = 'FortiWeb'

def is_waf(self):
    if self.matchcookie('FORTIWAFSID='):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        # Faced false positives hence reverting back to unique ones only
        if all(m in responsepage for m in (b'.fgd_icon', b'Client IP')):
            return True
    return False
