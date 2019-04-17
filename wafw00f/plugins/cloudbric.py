#!/usr/bin/env python


NAME = 'Cloudbric (Zendesk)'


def is_waf(self):
    # Approach reveals itself within the server headers without any mal requests
    if self.matchheader(('Server', 'Approach Web Application Firewall')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Cloudbric has nice characteristic blockpage, easy to detect.
        if any(i in page for i in (b'<title>Cloudbric | ERROR!', b'Your request was blocked by Cloudbric',
            b'please contact Cloudbric Support.', b'https://cloudbric.zendesk.com', b'Cloudbric Help Center')):
            return True
    return False