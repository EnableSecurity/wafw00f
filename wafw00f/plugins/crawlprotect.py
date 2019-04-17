#!/usr/bin/env python


NAME = 'CrawlProtect (Jean-Denis Brun)'


def is_waf(self):
    if self.matchcookie(r'^crawlprotecttag='):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # CrawlProtect exposes itself in title as well as page content
        if any(i in page for i in (b'<title>CrawlProtect', b'This site is protected by CrawlProtect')):
            return True
    return False