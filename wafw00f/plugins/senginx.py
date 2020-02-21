#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SEnginx (Neusoft)'


def is_waf(self):
    schemes = [
        self.matchContent(r'SENGINX\-ROBOT\-MITIGATION')
    ]
    if any(i for i in schemes):
        return True
    return False