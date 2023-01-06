#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Shield Security (One Dollar Plugin)'


def is_waf(self):
    if self.matchContent(r"You were blocked by the Shield"):
        return True

    if self.matchContent(r"remaining transgression\(s\) against this site"):
        return True

    if self.matchContent(r"Something in the URL.{0,5}?Form or Cookie data wasn\'t appropriate"):
        return True

    return False
