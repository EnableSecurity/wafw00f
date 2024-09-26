#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SecKing (SecKing)'


def is_waf(self):
    if self.matchHeader(('Server', r'secking(.?waf)?')):
        return True

    return False
