#!/usr/bin/env python


NAME = 'AnYu (AnYu Technologies)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'Sorry! your access has been intercepted by AnYu', 
            b'AnYu- the green channel')):
            return True
    return False