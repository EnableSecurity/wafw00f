#!/usr/bin/env python

# Well this is confusing, Sitelock itself uses Incapsula from Imperva
# So the fingerprints obtained on blockpage are exactly similar to those of Incapsula.
NAME = 'UTM Web Protection (Sophos)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # These fingerprints are the ones found in UTM 9 overall, block with debug mode
        # enabled as well as disabled.
        if any(i in page for i in (b'http://www.sophos.com', b'UTM')):
            return True
        # These are fingerprints when the debug mode is not enabled
        if any(i in page for i in (b'Powered by Sophos', b'Powered by UTM Web Protection')):
            return True
        # These fingerprints are those when debug mode is enabled in the WAF
        # So many fingerprints for narrowing down the detecting stuff
        if all(i in page for i in (b'<title>Access to the requested URL was blocked', 
            b'Access to the requested URL was blocked', b'incident was logged with the following log identifier', b'Inbound Anomaly Score Exceeded', b'Your cache administrator is')):
            return True
    return False