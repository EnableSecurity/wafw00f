#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloud Protector (Rohde & Schwarz CyberSecurity)'

def is_waf(self):
    if self.matchContent(r'Cloud Protector.*?by Rohde.{3,8}?Schwarz Cybersecurity'):
        return True

    if self.matchContent(r"<a href='https?:\/\/(?:www\.)?cloudprotector\.com\/'>R.{1,6}?S.Cloud Protector"):
        return True

    return False
