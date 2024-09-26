#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Alert Logic (Alert Logic)'


def is_waf(self):
    if not self.matchContent(r'<(title|h\d{1})>requested url cannot be found'):
        return False

    if not self.matchContent(r'we are sorry.{0,10}?but the page you are looking for cannot be found'):
        return False

    if not self.matchContent(r'back to previous page'):
        return False

    if not self.matchContent(r'proceed to homepage'):
        return False

    if not self.matchContent(r'reference id'):
        return False

    return True
