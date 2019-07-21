#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WP Cerber Security (Cerber Tech)'


def is_waf(self):
    schemes = [
        self.matchContent(r'your.request.looks.suspicious.or.similar.to.automated'),
        self.matchContent(r'our.server.stopped.processing.your.request'),
        self.matchContent(r'We.re.sorry.+you.are.not.allowed.to.proceed'),
        self.matchContent(r'requests.from.spam.posting.software'),
        self.matchContent(r'<title>403.Access.Forbidden')
        ]
    if all(i for i in schemes):
        return True
    return False