#!/usr/bin/env python


NAME = 'Aqtronix WebKnight'


def is_waf(self):
    detected = False
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, _ = r
        if response.status == 999:
            detected = True
            break
    return detected
