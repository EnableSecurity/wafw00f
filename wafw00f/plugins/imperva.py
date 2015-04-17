#!/usr/bin/env python


NAME = 'Imperva SecureSphere'


def is_waf(self):
    # thanks to Mathieu Dessus <mathieu.dessus(a)verizonbusiness.com> for this
    # might lead to false positives so please report back to sandro@enablesecurity.com
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsebody = r
        if response.version == 10:
            return True
    return False
