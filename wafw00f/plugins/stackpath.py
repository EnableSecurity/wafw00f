#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'StackPath (StackPath)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'<title>StackPath[^<]+</title>'),
        self.matchContent(r'Protected by <a href="https?:\/\/(?:www\.)?stackpath\.com\/"[^>]+>StackPath')
    ]

    schema2 = [
        self.matchContent(r"is using a security service for protection against online attacks"),
        self.matchContent(r'An action has triggered the service and blocked your request')
    ]

    if any(i for i in schema1):
        return True

    if all(i for i in schema2):
        return True

    return False