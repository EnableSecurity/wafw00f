#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloud Protector (Rohde & Schwarz CyberSecurity)'

def is_waf(self):
    schemes = [
        self.matchContent(r'Cloud Protector.*by Rohde &amp; Schwarz Cybersecurity')
    ]
    if any(i for i in schemes):
        return True
    return False
