#!/usr/bin/env python


NAME = 'Reblaze (Reblaze)'


def is_waf(self):
    if self.matchcookie(r'^rbzid='):
        return True
    if self.matchheader(('Server', 'Reblaze Secure Web Gateway')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if all(i in page for i in (b'Current session has been terminated', b'do not hesitate to contact us', 
            b'Access denied (403)')):
            return True
    return False