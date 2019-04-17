#!/usr/bin/env python


NAME = 'Varnish (OWASP)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # This often displayed when the debug mode is enabled.
        # Otherwise it is the regular 403vblockpage itself.
        if b'Request rejected by xVarnish-WAF' in page:
            return True
    return False