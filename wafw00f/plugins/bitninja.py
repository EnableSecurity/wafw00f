#!/usr/bin/env python


NAME = 'BitNinja (BitNinja)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Both signatures are contained within response, so checking for any one of them
        if any(i in page for i in (b'Security check by BitNinja', b'<title>Visitor anti-robot validation</title>')):
            return True
    return False