#!/usr/bin/env python


NAME = 'Zenedge (Zenedge)'


def is_waf(self):
    if self.matchheader(('Server', 'ZENEDGE')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        if b'/__zenedge/' in page:
            return True
        if response.getheader('X-Zen-Fury'):
            return True
    return False