#!/usr/bin/env python


NAME = 'WebARX (WebARX Security Solutions)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'WebARX</a> Web Application Firewall', b'www.webarxsecurity.com',
            b'/wp-content/plugins/webarx/includes/')):
            return True
    return False