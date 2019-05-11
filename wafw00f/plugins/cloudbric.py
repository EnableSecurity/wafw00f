#!/usr/bin/env python


NAME = 'Cloudbric (Penta Security)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Cloudbric has nice characteristic blockpage, easy to detect.
        # Obtained a new variant of the blockpage offered by CloudBric. Diff. attack methods result in diff fingerprints
        if any(i in page for i in (b'<title>Cloudbric | ERROR!', b'Your request was blocked by Cloudbric', b'<title>ERROR! |',
            b'please contact Cloudbric Support.', b'https://cloudbric.zendesk.com', b'Cloudbric Help Center', 
            b'malformed request syntax, invalid request message framing, or deceptive request routing.')):
            return True
    return False
