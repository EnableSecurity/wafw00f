#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'West263 Content Delivery Network'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Cache', r'(.+)?W(S)?T263CDN'))
    ]
    if any(i for i in schemes):
        return True
    return False