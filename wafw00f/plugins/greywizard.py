#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Greywizard (Grey Wizard)'


def is_waf(self):
    if self.matchHeader(('Server', 'greywizard')):
        return True

    if self.matchContent(r'<(title|h\d{1})>Grey Wizard'):
        return True

    if self.matchContent(r'contact the website owner or Grey Wizard'):
        return True

    if self.matchContent(r'We.ve detected attempted attack or non standard traffic from your ip address'):
        return True

    return False
