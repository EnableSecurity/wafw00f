#!/usr/bin/env python


NAME = 'Airlock (Phion/Ergon)'


def is_waf(self):
    # This method of detection is old (though most reliable), 
    # so we check it first
    if self.matchcookie(r'^AL[_-]?(SESS|LB)='):
        return True
    # Nowadays many sites running Airlock do not set cookies 
    # directly without authentication. So we have to make the 
    # last final check of the characteristic block page.
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        if all(a in responsepage for a in (b"Check your request and all parameters", 
            b"Bad Request", b"The server detected a syntax error in your request")):
            return True
    return False