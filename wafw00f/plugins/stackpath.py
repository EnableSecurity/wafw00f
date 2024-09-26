#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'StackPath (StackPath)'


def is_waf(self):
    if check_schema_01(self):
        return True

    if check_schema_02(self):
        return True

    return False


def check_schema_01(self):
    if self.matchContent(r'<title>StackPath[^<]+</title>'):
        return True

    if self.matchContent(r'Protected by <a href="https?:\/\/(?:www\.)?stackpath\.com\/"[^>]+>StackPath'):
        return True

    return False


def check_schema_02(self):
    if not self.matchContent(r"is using a security service for protection against online attacks"):
        return False

    if not self.matchContent(r'An action has triggered the service and blocked your request'):
        return False

    return True
