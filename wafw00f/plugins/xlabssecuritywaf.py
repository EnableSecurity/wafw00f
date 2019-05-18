#!/usr/bin/env python

NAME = 'XLabs Security WAF (XLabs)'

def is_waf(self):
    if self.matchheader(('x-cdn', 'XLabs Security')):
        return True
    # This is another fingerprint header found in a different site
    # during extensive testing for this plugin.
    if self.matchheader(('Secured', r'^By XLabs Security.+?')):
        return True
    # Another nice fingerprint found where server returns attack
    # header as 'Server: XLabs WAF v3.0 http://www.xlabs.com.br/waf'
    if self.matchheader(('Server', r'^XLabs WAF.+?'), attack=True):
        return True
    return False
