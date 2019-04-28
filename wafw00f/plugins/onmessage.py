#!/usr/bin/env python


NAME = 'OnMessage Shield (BlackBaud)'


def is_waf(self):
    # Blackbaud reveals itself within X-Engine header
    if self.matchheader(('X-Engine', 'onMessage Shield')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # There are multiple fingerprints for this
        if any(i in page for i in (b'Blackbaud K-12 conducts routine maintenance', b'status.blackbaud.com'
            b'This site is protected by an enhanced security system', b'onMessage SHIELD', b'maintenance.blackbaud.com')):
            return True
    return False