#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudfloor (Cloudfloor DNS)'


def is_waf(self):
    if self.matchHeader(('Server', r'CloudfloorDNS(.WAF)?')):
        return True

    if self.matchContent(r'<(title|h\d{1})>CloudfloorDNS.{0,6}?Web Application Firewall Error'):
        return True

    if self.matchContent(r'www\.cloudfloordns\.com/contact'):
        return True

    return False
