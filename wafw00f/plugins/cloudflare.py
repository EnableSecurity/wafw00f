#!/usr/bin/env python


NAME = 'CloudFlare'


def is_waf(self):
	# This should be given first priority (most reliable)
    if self.matchcookie('__cfduid'):
        return True
    # Not all servers return sloudflare-nginx, only nginx ones
    if self.matchheader(('server', 'cloudflare-nginx')) or self.matchheader(('server', 'cloudflare')):
        return True
    return False
