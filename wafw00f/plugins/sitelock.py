#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sitelock (TrueShield)'

# Well this is confusing, Sitelock itself uses Incapsula from Imperva
# So the fingerprints obtained on blockpage are similar to those of Incapsula.

def is_waf(self):
    if self.matchContent(r"SiteLock will remember you"):
        return True

    if self.matchContent(r"Sitelock is leader in Business Website Security Services"):
        return True

    if self.matchContent(r"sitelock[_\-]shield([_\-]logo|[\-_]badge)?"):
        return True

    if self.matchContent(r'SiteLock incident ID'):
        return True

    return False
