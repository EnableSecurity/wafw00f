#!/usr/bin/env python


NAME = 'Secure Entry (United Security Providers)'


def is_waf(self):
    # Secure Entry nicely expresses itself within the server header
    # No malicious requests required.
    if self.matchheader(('Server', 'Secure Entry Server')):
        return True
    return False