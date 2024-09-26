#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudbric (Penta Security)'


def is_waf(self):
    if self.matchContent(r'<title>Cloudbric.{0,5}?ERROR!'):
        return True

    if self.matchContent(r'Your request was blocked by Cloudbric'):
        return True

    if self.matchContent(r'please contact Cloudbric Support'):
        return True

    if self.matchContent(r'cloudbric\.zendesk\.com'):
        return True

    if self.matchContent(r'Cloudbric Help Center'):
        return True

    if self.matchContent(r'malformed request syntax.{0,4}?invalid request message framing.{0,4}?or deceptive request routing'):
        return True

    return False
