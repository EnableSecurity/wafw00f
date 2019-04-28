#!/usr/bin/env python


NAME = 'Greywizard (Grey Wizard)'


def is_waf(self):
    # Grey Wizard has a nice way of expressing itself in server header
    if self.matchheader(('Server', 'greywizard')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Sites without modified block page return all fingerprints, so checking for any one of them works.
        if any(i in page for i in (b'<title>Grey Wizard</title>', b'Contact the website owner or Grey Wizard',
            b"We've detected attempted attack or non standard traffic from your IP address")):
            return True
    return False