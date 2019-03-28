#!/usr/bin/env python

NAME = 'Radware AppWall'

def is_waf(self):
    if self.matchheader(('X-SL-CompState', '.')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsebody = r
        # Most reliable fingerprint is this on block page
        if all(i in responsebody for i in (b'because we have detected unauthorized activity', 
            b'<TITLE>Unauthorized Request Blocked</TITLE>', b'mailto:CloudWebSec@radware.com')):
            return True
    return False
