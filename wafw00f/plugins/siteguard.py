#!/usr/bin/env python


NAME = 'SiteGuard (Sakura Inc.)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'Powered by SiteGuard', b'The server refuse to browse the page')):
            return True
    return False