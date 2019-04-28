#!/usr/bin/env python


NAME = 'Newdefend (NewDefend)'


def is_waf(self):
    # Newdefend reveals itself within the server headers without any mal requests
    if self.matchheader(('Server', 'Newdefend')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'http://www.newdefend.com/feedback', b'/nd-block/')):
            return True
    return False