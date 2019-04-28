#!/usr/bin/env python


NAME = 'aeSecure (aeSecure)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        if response.getheader('aeSecure-code'):
            return True
        if b'aesecure_denied.png' in page:
            return True
    return False