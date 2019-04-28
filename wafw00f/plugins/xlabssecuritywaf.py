#!/usr/bin/env python

NAME = 'XLabs Security WAF (XLabs)'

def is_waf(self):
    if self.matchheader(('x-cdn', 'XLabs Security')):
        return True
    # Another nice fingerprint found where server returns a
    # header as 'Server: XLabs WAF v3.0 http://www.xlabs.com.br/waf'
    if self.matchheader(('server', r'XLabs WAF(.*)?')):
        return True
    return False