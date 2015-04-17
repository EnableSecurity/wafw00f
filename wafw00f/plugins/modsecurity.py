#!/usr/bin/env python


NAME = 'Trustwave ModSecurity'


def is_waf(self):
    detected = False
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsebody = r
        if response.status == 501:
            detected = True
            break
    # the following based on nmap's http-waf-fingerprint.nse
    if self.matchheader(('server', '(mod_security|Mod_Security|NOYB)')):
        return True
    return detected
