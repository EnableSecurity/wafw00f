#!/usr/bin/env python


NAME = 'Approach (Approach)'


def is_waf(self):
    # Approach reveals itself within the server headers without any mal requests
    if self.matchheader(('Server', 'Approach Web Application Firewall')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Sites without modified block page return both, so checking for any
        # one of them works.
        if any(i in page for i in (b'Approach</b> Web Application Firewall', 
            b'Approach</i> infrastructure team')):
            return True
        # However sites with modified blockpage retain these two common 
        # characteristic fingerprints.
        if all(i in page for i in (b'Sorry for the inconvenience!', 
            b'If this was an legitimate request please contact us with details!')):
            return True
    return False