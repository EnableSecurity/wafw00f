#!/usr/bin/env python

NAME = 'Sucuri (Sucuri Inc.)'

def is_waf(self):
    # Fingerprints not needing any attack
    if self.matchheader(('X-Sucuri-ID', '.+')):
        return True
    if self.matchheader(('X-Sucuri-Cache', '.+')):
        return True
    if self.matchheader(('Server', 'Sucuri/Cloudproxy')):
        return True
    # Fingerprints under attack
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsebody = r
        # Most reliable fingerprint is this on block page
        if response.getheader('X-Sucuri-Block'):
            return True
        if any(i in responsebody for i in (b'Access Denied - Sucuri Website Firewall', 
            b'<title>Sucuri WebSite Firewall - Access Denied</title>', b'https://sucuri.net/privacy-policy', 
            b'https://cdn.sucuri.net/sucuri-firewall-block.css', b'Sucuri Inc.', b'cloudproxy@sucuri.net')):
            return True
    return False