#!/usr/bin/env python


NAME = 'CacheWall (Varnish)'


def is_waf(self):
    # Varnish CacheWALL nicely puts itself in various headers as below.
    if self.matchheader(('Server', 'Varnish')):
        return True
    if self.matchheader(('X-Varnish', '.+')):
        return True
    if self.matchheader(('X-Cachewall-Action', '.+')):
        return True
    if self.matchheader(('X-Cachewall-Reason', '.+')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # In-page fingerprints vary a lot in different sites. Hence these are not quite reliable.
        if any(i in page for i in (b'Security by Cachewall </span>', b'403 Naughty, not Nice!',
            b'Varnish cache Server')):
            return True
    return False