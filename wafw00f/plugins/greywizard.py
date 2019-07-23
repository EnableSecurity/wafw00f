#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Greywizard (Grey Wizard)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'greywizard')),
        self.matchContent(r'<.+>Grey Wizard<.+>'),
        self.matchContent(r'contact.the.website.owner.or.Grey.Wizard'),
        self.matchContent(r'We.?ve.detected.attempted.attack.or.non.standard.traffic.from.your.ip.address')
    ]
    if any(i for i in schemes):
        return True
    return False