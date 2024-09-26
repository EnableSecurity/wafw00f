#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'UEWaf (UCloud)'


def is_waf(self):
    if self.matchHeader(('Server', r'uewaf(/[0-9\.]+)?')):
        return True

    if self.matchContent(r'/uewaf_deny_pages/default/img/'):
        return True

    if self.matchContent(r'ucloud\.cn'):
        return True

    return False
