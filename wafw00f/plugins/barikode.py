#!/usr/bin/env python


NAME = 'Barikode (Ethic Ninja)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if b'<strong>BARIKODE</strong>' in page:
            return True
        # May return false positives but addition of h1 tags
        # around the caps narrowed it down to very rare chances.
        if b'<h1>FORBIDDEN ACCESS</h1><br>' in page:
            return True
    return False