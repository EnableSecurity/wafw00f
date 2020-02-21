#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sitelock (TrueShield)'

# Well this is confusing, Sitelock itself uses Incapsula from Imperva
# So the fingerprints obtained on blockpage are similar to those of Incapsula.

def is_waf(self):
    schemes = [
        self.matchContent(r"SiteLock will remember you"),
        self.matchContent(r"Sitelock is leader in Business Website Security Services"),
        self.matchContent(r"sitelock[_\-]shield([_\-]logo|[\-_]badge)?"),
        self.matchContent(r'SiteLock incident ID')
    ]
    if any(i for i in schemes):
        return True
    return False