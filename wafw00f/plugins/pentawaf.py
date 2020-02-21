#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'PentaWAF (Global Network Services)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'PentaWaf(/[0-9\.]+)?')),
        self.matchContent(r'Penta.?Waf/[0-9\.]+?.server')
    ]
    if any(i for i in schemes):
        return True
    return False