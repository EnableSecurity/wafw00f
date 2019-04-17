#!/usr/bin/env python

# Well this is confusing, Sitelock itself uses Incapsula from Imperva
# So the fingerprints obtained on blockpage are exactly similar to those of Incapsula.
NAME = 'Sitelock (TrueShield)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'SiteLock will remember you', b'SiteLock Incident ID',
            b'Sitelock is leader in Business Website Security Services', b'sitelock_shield_logo')):
            return True
    return False