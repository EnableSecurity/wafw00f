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
        if all(m in responsepage for m in (b'h2.fgd_icon', b'The page cannot be displayed',
            b'Please contact the administrator for additional information', b'URL:', b'Attack ID', b'Message ID', b'Client IP')):
            return True
    return False
