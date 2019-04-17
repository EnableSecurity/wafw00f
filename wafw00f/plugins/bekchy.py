#!/usr/bin/env python


NAME = 'Bekchy (Faydata Technologies Inc.)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Both signatures are contained within response, so checking for any one of them
        # Sometimes I observed that there is an XHR request being being made to submit the 
        # report data automatically upon page load. In those cases a missing https is causing
        # false negatives.
        if any(i in page for i in (b'Bekchy - Access Denied', b'bekchy.com/report')):
            return True
    return False