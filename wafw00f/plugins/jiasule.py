#!/usr/bin/env python


NAME = 'Jiasule (Jiasule)'


def is_waf(self):
    # Jiasule has a nice way of expressing itself in server header
    if self.matchheader(('Server', r'Jiasule\-WAF')):
        return True
    # It also expresses itself in cookies
    if self.matchcookie(r'^jsl_tracking'):
        return True
    if self.matchcookie(r'__jsluid='):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Both are standard fingerprints, so checking for any one works.
        if any(i in page for i in (b'notice-jiasule', b'static.jiasule.com')):
            return True
    return False