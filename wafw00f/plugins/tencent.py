#!/usr/bin/env python


NAME = 'Tencent Cloud Firewall (Tencent Technologies)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'waf.tencent-cloud.com/' in page:
            return True
    return False