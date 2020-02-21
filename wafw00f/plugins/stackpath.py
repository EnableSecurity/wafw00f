#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'StackPath (StackPath)'


def is_waf(self):
    schemes = [
        self.matchContent(r"This website is using a security service to protect itself"),
        self.matchContent(r'You performed an action that triggered the service and blocked your request')
    ]
    if all(i for i in schemes):
        return True
    return False