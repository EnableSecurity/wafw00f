#!/usr/bin/env python


NAME = 'Citrix NetScaler'


def is_waf(self):
    """
    First checks if a cookie associated with Netscaler is present,
    if not it will try to find if a "Cneonction" or "nnCoection" is returned
    for any of the attacks sent
    """
    # Cookies are set only when someone is authenticated.
    # Not much reliable since wafw00f isn't authenticating.
    if self.matchcookie('^(ns_af=|citrix_ns_id|NSC_)'):
        return True
    # Not quite sure about this, may return false positives, not
    # one of the sites I've met returned this header
    if self.matchheader(('Location', '\\/vpn\\/index\\.html')):
        return True
    # The actual fngerprints are obtained upon attack in source.
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsepage = r
        if any(a in responsepage for a in (b"NS Transaction ID:", b"AppFW Session ID:",
            b'Violation Category: APPFW_', b'Citrix|NetScaler')):
            return True
        # Reliable but not all servers return this header
        if self.matchheader(('Via', 'NS-CACHE')):
            return True
        if self.matchheader(('Cneonction', 'close')):
            return True
        if self.matchheader(('nnCoection', 'close')):
            return True
    return False
