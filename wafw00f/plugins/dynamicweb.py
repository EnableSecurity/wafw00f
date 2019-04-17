#!/usr/bin/env python


NAME = 'DynamicWeb Injection Check (DynamicWeb)'


def is_waf(self):
    if self.matchcookie('crawlprotecttag'):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, _ = r
        if response.getheader('X-403-Status-By') and response.status == 403:
            return True
    return False