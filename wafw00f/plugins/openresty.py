#!/usr/bin/env python


NAME = 'Open-Resty Lua Nginx WAF'


def is_waf(self):
    detected1 = False
    detected2 = False
    # Checking if server header is running open-resty
    if self.matchheader(('Server', r'^openresty/.+?')):
        detected1 = True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        if response.status == 406 and b'openresty/' in page:
            return True
        # Sometimes the blockpage is the default 403 page.
        if response.status == 403:
            detected2 = True
        # If both have returned True, then... we know it is behind the WAF.
        if detected1 and detected2:
            return True
    return False
