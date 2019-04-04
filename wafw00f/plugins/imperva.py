#!/usr/bin/env python


NAME = 'Imperva SecureSphere'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        # this is more reliable fingerprint, the standard error page
        if all(m in page for m in (b'<H2>Error</H2>', b'<title>Error</title>', b'The incident ID is:',
             b"This page can't be displayed.", b"Contact support for additional information.")):
            return True
        # never met a site returning this, but still considered keeping it
        # might lead to false positives
        if response.version == 10:
            return True
    return False