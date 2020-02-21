#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudbric (Penta Security)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>Cloudbric.{0,5}?ERROR!'),
        self.matchContent(r'Your request was blocked by Cloudbric'),
        self.matchContent(r'please contact Cloudbric Support'),
        self.matchContent(r'cloudbric\.zendesk\.com'),
        self.matchContent(r'Cloudbric Help Center'),
        self.matchContent(r'malformed request syntax.{0,4}?invalid request message framing.{0,4}?or deceptive request routing')
    ]
    if any(i for i in schemes):
        return True
    return False