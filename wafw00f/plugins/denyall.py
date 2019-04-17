#!/usr/bin/env python


NAME = 'DenyALL (Rohde & Schwarz CyberSecurity)'


def is_waf(self):
    # Tested against a Rweb 3.8
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, _ = r
        if response.status == 200 and response.reason == 'Condition Intercepted':
            return True
    return False