#!/usr/bin/env python


NAME = 'Bekchy (Faydata Technologies Inc.)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Both signatures are contained within response, so checking for any one of them
        if any(i in page for i in (b'Bekchy - Access Denied', b'https://bekchy.com/report')):
            return True
    return False