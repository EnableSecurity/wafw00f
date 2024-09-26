#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BinarySec (BinarySec)'


def is_waf(self):
    if self.matchHeader(('Server', 'BinarySec')):
        return True

    if self.matchHeader(('x-binarysec-via', '.+')):
        return True

    if self.matchHeader(('x-binarysec-nocache', '.+')):
        return True

    return False
