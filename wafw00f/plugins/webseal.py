#!/usr/bin/env python


NAME = 'WebSEAL (IBM)'


def is_waf(self):
    if self.matchheader(('Server', 'WebSEAL')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # The first fingerprint is for unconfigured blockpages
        if any(i in page for i in (b'This is a WebSEAL error message template file', b'WebSEAL server received an invalid HTTP request')):
            return True
    return False