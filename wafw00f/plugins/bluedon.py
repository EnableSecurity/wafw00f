#!/usr/bin/env python


NAME = 'Bluedon (Bluedon IST)'


def is_waf(self):
    # Found sample servers returning 'Server: BDWAF/2.0'
    if self.matchheader(('Server', r'BDWAF(.*)?')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'Bluedon Web Application Firewall' in page:
            return True
    return False