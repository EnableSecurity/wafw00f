#!/usr/bin/env python


NAME = 'WebTotem (WebTotem)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # WebTotem returns its name in blockpage
        if all(i in page for  i in (b'The current request was blocked', b'WebTotem')):
            return True
    return False