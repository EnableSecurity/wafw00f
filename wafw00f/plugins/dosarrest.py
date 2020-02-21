#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DOSarrest (DOSarrest Internet Security)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-DIS-Request-ID', '.+')),
        # Found samples of DOSArrest returning 'Server: DoSArrest/3.5'
        self.matchHeader(('Server', r'DOSarrest(.*)?'))
    ]
    if any(i for i in schemes):
        return True
    return False