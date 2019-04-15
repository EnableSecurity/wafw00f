#!/usr/bin/env python


NAME = 'TransIP Firewall'


def is_waf(self):
    # TransIP WAF has these two firewall fingerprints.
    # The blockpage is the regular 403 page, no fingerprints
    # on blockpage.
    if self.matchheader(('X-TransIP-Backend', '.+')):
        return True
    if self.matchheader(('X-TransIP-Balancer', '.+')):
        return True
    return False