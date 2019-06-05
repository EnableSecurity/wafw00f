#!/usr/bin/env python


NAME = 'WTS-WAF (WTS)'


def is_waf(self):
    # There are sites which are found to return 'Server: wts/1.2'
    if self.matchheader(('Server', r'wts(.+)?')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # WTS returns its name in blockpage
        if any(i in page for  i in (b'<h1>WTS-WAF', b'<title>WTS-WAF')):
            return True
    return False