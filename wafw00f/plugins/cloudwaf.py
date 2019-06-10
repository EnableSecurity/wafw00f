#!/usr/bin/env python
NAME = 'CloudWAF-TJH/US-SECKING)'
def is_waf(self):
    # CloudWAF exposes itself below the Forbidden Header
    if self.matchheader(('Server', 'CloudWAF-TJH/US-SECKING')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'CloudWAF/' in page:
            return True
    return False
