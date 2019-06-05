#!/usr/bin/env python


NAME = 'LiteSpeed Firewall (LiteSpeed Technologies)'


def is_waf(self):
    if self.matchheader(('Server', 'LiteSpeed')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'Proudly powered by LiteSpeed Web Server', b'www.litespeedtech.com/error-page',
            b'Access to resource on this server is denied')):
            return True
    return False