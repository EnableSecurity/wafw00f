#!/usr/bin/env python


NAME = 'Cloudflare (Cloudflare Inc.)'


def is_waf(self):
    # This should be given first priority (most reliable)
    if self.matchcookie('__cfduid'):
        return True
    # Not all servers return cloudflare-nginx, only nginx ones
    if self.matchheader(('server', 'cloudflare-nginx')) or self.matchheader(('server', 'cloudflare')):
        return True
    # Found a new nice fingerprint for cloudflare
    if self.matchheader(('cf-ray', '.*')):
        return True
    return False