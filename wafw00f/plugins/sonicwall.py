#!/usr/bin/env python


NAME = 'SonicWall (Dell)'


def is_waf(self):
    # Sonicwall exposes itself within server headers
    if self.matchheader(('Server', 'SonicWALL')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # This is the funny part :p
        if all(i in page for i in (b'<title>Web Site Blocked</title>', b'nsa_banner')):
            return True
    return False