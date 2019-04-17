#!/usr/bin/env python


NAME = 'FirePass (F5 Networks)'


def is_waf(self):    
    if self.matchheader(('Location', r'\/my\.logon\.php3')) and self.matchcookie('^VHOST'):
        return True
    elif self.matchcookie(r'^MRHSession') and (self.matchcookie(r'^VHOST') or self.matchcookie(r'^uRoamTestCookie')):
        return True
    elif self.matchcookie(r'^MRHSession') and (self.matchcookie(r'^MRHCId') or self.matchcookie(r'^MRHIntranetSession')):
        return True
    elif self.matchcookie(r'^uRoamTestCookie') or self.matchcookie(r'^VHOST'):
        return True
    else:
        return False