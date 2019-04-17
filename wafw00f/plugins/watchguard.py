#!/usr/bin/env python


NAME = 'WatchGuard (WatchGuard Technologies)'


def is_waf(self):
    # Not all servers return this as server header
    if self.matchheader(('Server', 'WatchGuard')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'Request denied by WatchGuard Firewall', b'WatchGuard Technologies Inc.')):
            return True
    return False
# NOTE: WatchGuard is not actually a WAF but functions as one. It is a IPS in reality.