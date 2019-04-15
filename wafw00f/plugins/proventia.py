#!/usr/bin/env python


NAME = 'Proventia'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'request does not match Proventia rules' in page:
            return True
    return False