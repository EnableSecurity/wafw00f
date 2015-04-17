#!/usr/bin/env python


NAME = 'F5 FirePass'


def is_waf(self):
    detected = False
    if self.matchheader(('Location', '\/my\.logon\.php3')) and self.matchcookie('^VHOST'):
        return True
    elif self.matchcookie('^MRHSession') and (self.matchcookie('^VHOST') or self.matchcookie('^uRoamTestCookie')):
        return True
    elif self.matchcookie('^MRHSession') and (self.matchcookie('^MRHCId') or self.matchcookie('^MRHIntranetSession')):
        return True
    elif self.matchcookie('^uRoamTestCookie') or self.matchcookie('^VHOST'):
        return True
    else:
        return False
