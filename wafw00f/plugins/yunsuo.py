#!/usr/bin/env python


NAME = 'Yunsuo (Yunsuo)'


def is_waf(self):
    if self.matchcookie(r'^yunsuo_session'):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'yunsuologo' in page:
            return True
    return False