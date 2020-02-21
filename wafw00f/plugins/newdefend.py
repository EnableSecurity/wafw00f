#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Newdefend (NewDefend)'


def is_waf(self):
    schemes = [
        # This header can be obtained without attack mode
        # Most reliable fingerprint
        self.matchHeader(('Server', 'Newdefend')),
        # Reliable ones within blockpage
        self.matchContent(r'www\.newdefend\.com/feedback'),
        self.matchContent(r'/nd\-block/')
    ]
    if any(i for i in schemes):
        return True
    return False