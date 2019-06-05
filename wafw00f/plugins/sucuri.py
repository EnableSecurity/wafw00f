#!/usr/bin/env python

NAME = 'Sucuri CloudProxy (Sucuri Inc.)'

def is_waf(self):
    # Fingerprints not needing any attack
    if self.matchheader(('X-Sucuri-ID', r'.+?')):
        return True
    if self.matchheader(('X-Sucuri-Cache', r'.+?')):
        return True
    if self.matchheader(('Server', r'Sucuri(.Cloudproxy)?')):
        return True
    # Fingerprints under attack
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsebody = r
        # Most reliable fingerprint is this amongst headers
        if response.getheader('X-Sucuri-Block'):
            return True
        if any(i in responsebody for i in (b'Access Denied - Sucuri Website Firewall', 
            b'<title>Sucuri WebSite Firewall - Access Denied</title>', b'sucuri.net/privacy-policy', 
            b'cdn.sucuri.net/sucuri-firewall-block.css', b'Sucuri Inc.', b'cloudproxy@sucuri.net')):
            return True
    return False