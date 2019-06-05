#!/usr/bin/env python


NAME = 'NexusGuard Firewall (NexusGuard)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'<p>Powered by Nexusguard', b'nexusguard.com/wafpage/index.html#403;')):
            return True
    return False