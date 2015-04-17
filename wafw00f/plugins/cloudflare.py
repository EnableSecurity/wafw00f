#!/usr/bin/env python


NAME = 'CloudFlare'


# the following based on nmap's http-waf-fingerprint.nse
def is_waf(self):
    if self.matchheader(('server', 'cloudflare-nginx')):
        return True
    if self.matchcookie('__cfduid'):
        return True
    return False
