#!/usr/bin/env python


NAME = 'Safedog (SafeDog)'


def is_waf(self):
    if self.matchcookie(r'^safedog\-flow\-item='):
        return True
    if self.matchheader(('server', 'Safedog')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsebody = r
        # Most reliable fingerprint is this on block page
        if any(i in responsebody for i in (b'safedogsite/broswer_logo.jpg', 
            b'404.safedog.cn/sitedog_stat.html', b'404.safedog.cn/images/safedogsite/head.png')):
            return True
    return False