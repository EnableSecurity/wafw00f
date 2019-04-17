#!/usr/bin/env python


NAME = 'Alert Logic (Alert Logic)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if all(i in page for i in (b'<title>Requested URL cannot be found</title>', b'Proceed to homepage',
            b'Back to previous page', b'We are sorry, but the page you are looking for cannot be found', 
            b'Reference ID:', b'The page has either been removed, renamed or is temporarily unavailable')):
            return True
    return False