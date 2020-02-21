#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Shield Security (One Dollar Plugin)'


def is_waf(self):
    schemes = [
        self.matchContent(r"You were blocked by the Shield"),
        self.matchContent(r"remaining transgression\(s\) against this site"),
        self.matchContent(r"Something in the URL.{0,5}?Form or Cookie data wasn\'t appropriate")
    ]
    if any(i for i in schemes):
        return True
    return False