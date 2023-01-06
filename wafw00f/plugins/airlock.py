#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Airlock (Phion/Ergon)'


def is_waf(self):
    # This method of detection is old (though most reliable), so we check it first
    if self.matchCookie(r'^al[_-]?(sess|lb)='):
        return True

    if self.matchContent(r'server detected a syntax error in your request'):
        return True

    return False
