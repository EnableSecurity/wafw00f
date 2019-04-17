#!/usr/bin/env python


NAME = 'ZScaler (Accenture)'


def is_waf(self):
    # ZScaler has its own server header set
    if self.matchheader(('Server', 'ZScaler')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # ZScaler has lot of fingerprints in its blockpage, here are some
        if any(i in page for  i in (b'Access Denied: Accenture Policy', b'policies.accenture.com',
            b'login.zscloud.net/img_logo_new1.png', b'Zscaler to protect you from internet threats',
            b"Accenture's webfilters indicate that the site likely contains content considered inappropriate")):
            return True
    return False