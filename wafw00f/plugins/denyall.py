#!/usr/bin/env python


NAME = 'DenyALL WAF'


def is_waf(self):
    if self.matchcookie('^sessioncookie='):
        return True
    # Tested against a Rweb 3.8
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, _ = r
        if response.status == 200 and response.reason == 'Condition Intercepted':
            return True
    return False
