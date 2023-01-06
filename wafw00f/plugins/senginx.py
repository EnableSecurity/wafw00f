#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SEnginx (Neusoft)'


def is_waf(self):
    if self.matchContent(r'SENGINX\-ROBOT\-MITIGATION'):
        return True

    return False
