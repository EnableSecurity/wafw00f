#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloud Protector (Rohde & Schwarz CyberSecurity)'

def is_waf(self):
    schemes = [
        self.matchContent(r'Cloud Protector.*?by Rohde.{3,8}?Schwarz Cybersecurity'),
        self.matchContent(r"<a href='https?:\/\/(?:www\.)?cloudprotector\.com\/'>R.{1,6}?S.Cloud Protector")
    ]
    if any(i for i in schemes):
        return True
    return False
