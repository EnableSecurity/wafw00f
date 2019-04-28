#!/usr/bin/env python


NAME = 'WP Cerber Security (Cerber Tech)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if all(i in page for i in (b'Your request looks suspicious or similar to automated', 
            b'Our server stopped processing your request', b"We're sorry, you are not allowed to proceed",
            b'requests from spam posting software', b'<title>403 Access Forbidden</title>')):
            return True
    return False