#!/usr/bin/env python


NAME = 'NetScaler AppFirewall (Citrix Systems)'


def is_waf(self):
    # This header can be obtained without attack mode
    if self.matchheader(('Via', r'NS\-CACHE')):
        return True
    # Cookies are set only when someone is authenticated.
    # Not much reliable since wafw00f isn't authenticating.
    if self.matchcookie(r'^(ns_af=|citrix_ns_id|NSC_)'):
        return True
    # Not quite sure about this, may return false positives, not
    # one of the sites I've met returned this header
    if self.matchheader(('Location', r'\/vpn\/index\.html')):
        return True
    # The actual fingerprints are obtained upon attack in source.
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsepage = r
        if any(a in responsepage for a in (b"NS Transaction ID:", b"AppFW Session ID:",
            b'Violation Category: APPFW_', b'Citrix|NetScaler')):
            return True
        # Reliable but not all servers return this header
        if response.getheader('Cneonction'):
            return True
        if response.getheader('nnCoection'):
            return True
    return False