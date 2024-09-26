#!/usr/bin/env python
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Azure Application Gateway (Microsoft)'


def is_waf(self):
    if self.matchContent(r'<center>Microsoft-Azure-Application-Gateway/v2</center>') and \
        self.matchContent(r'<h1>403 Forbidden</h1>'):
        return True

    return False
