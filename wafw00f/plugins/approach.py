#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Approach (Approach)'


def is_waf(self):
    # This method of detection is old (though most reliable), so we check it first
    if self.matchContent(r'approach.{0,10}?web application (firewall|filtering)'):
        return True

    if self.matchContent(r'approach.{0,10}?infrastructure team'):
        return True

    return False
