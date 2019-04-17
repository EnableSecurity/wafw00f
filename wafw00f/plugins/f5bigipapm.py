#!/usr/bin/env python


NAME = 'BIG-IP Access Policy Manager (F5 Networks)'


def is_waf(self):
    # the following based on nmap's http-waf-fingerprint.nse
    if self.matchcookie(r'^LastMRH_Session') and self.matchcookie(r'^MRHSession'):
        return True
    elif self.matchheader(('server', r'BigIP|BIG-IP|BIGIP')) and self.matchcookie(r'^MRHSession'):
        return True
    if self.matchheader(('Location', r'\/my.policy')) and self.matchheader(('server', r'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchheader(('Location', r'\/my\.logout\.php3')) and self.matchheader(('server', r'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchheader(('Location', r'.+\/f5\-w\-68747470.+')) and self.matchheader(('server', r'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchheader(('server', r'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchcookie(r'^F5_fullWT') or self.matchcookie(r'^F5_ST') or self.matchcookie(r'^F5_HT_shrinked'):
        return True
    elif self.matchcookie(r'^MRHSequence') or self.matchcookie(r'^MRHSHint') or self.matchcookie(r'^LastMRH_Session'):
        return True
    else:
        return False