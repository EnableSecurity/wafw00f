#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Alert Logic (Alert Logic)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<(title|h\d{1})>requested url cannot be found'),
        self.matchContent(r'we are sorry.{0,10}?but the page you are looking for cannot be found'),
        self.matchContent(r'back to previous page'),
        self.matchContent(r'proceed to homepage'),
        self.matchContent(r'reference id'),
        ]
    if all(i for i in schemes):
        return True
    return False