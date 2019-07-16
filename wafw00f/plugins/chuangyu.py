#!/usr/bin/env python


NAME = 'Chuang Yu Shield (Yunaq)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Both reference to URLs in blockpage
        if any(i in page for i in (b'www.365cyd.com', b'help.365cyd.com/cyd-error-help.html?code=403')):
            return True
    return False