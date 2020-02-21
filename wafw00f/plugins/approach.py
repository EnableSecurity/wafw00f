#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Approach (Approach)'


def is_waf(self):
    schemes = [
        # This method of detection is old (though most reliable), so we check it first
        self.matchContent(r'approach.{0,10}?web application (firewall|filtering)'),
        self.matchContent(r'approach.{0,10}?infrastructure team')
        ]
    if any(i for i in schemes):
        return True
    return False