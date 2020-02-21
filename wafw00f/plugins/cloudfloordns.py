#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudfloor (Cloudfloor DNS)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'CloudfloorDNS(.WAF)?')),
        self.matchContent(r'<(title|h\d{1})>CloudfloorDNS.{0,6}?Web Application Firewall Error'),
        self.matchContent(r'www\.cloudfloordns\.com/contact')
    ]
    if any(i for i in schemes):
        return True
    return False