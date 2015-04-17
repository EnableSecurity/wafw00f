#!/usr/bin/env python


NAME = 'DenyALL WAF'


def is_waf(self):
    # credit goes to W3AF
    if self.matchcookie('^sessioncookie='):
        return True
    # credit goes to Sebastien Gioria
    #   Tested against a Rweb 3.8
    # and modified by sandro gauci and someone else
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsebody = r
        if response.status == 200:
            if response.reason == 'Condition Intercepted':
                return True
    return False
