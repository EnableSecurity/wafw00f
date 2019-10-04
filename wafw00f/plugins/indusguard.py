#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'IndusGuard (Indusface)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'IF_WAF')),
        self.matchContent(r'This website is secured against online attacks. Your request was blocked'),
        self.matchContent(r'(?s)Client.IP.+?Incident.Time.+?Incident.ID')
    ]
    if any(i for i in schemes):
        return True
    return False