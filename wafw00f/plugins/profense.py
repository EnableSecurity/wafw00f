#!/usr/bin/env python


NAME = 'Profense (ArmorLogic)'


def is_waf(self):
    if self.matchheader(('Server', 'profense')):
        return True
    if self.matchcookie(r'^PLBSID='):
        return True
    return False