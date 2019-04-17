#!/usr/bin/env python


NAME = 'SEnginx (Neusoft)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'SENGINX-ROBOT-MITIGATION' in page:
            return True
    return False