
#!/usr/bin/env python


NAME = 'CloudLinux Imunify360'


def is_waf(self):
    # Imunify has a nice way of expressing itself in server header
    if self.matchheader(('Server', 'imunify360-webshield')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Sites without modified block page return all fingerprints, so checking for any one of them works.
        if any(i in page for i in (b'protected by Imunify360', b'Powered by Imunify360', b'imunify360 preloader')):
            return True
    return False