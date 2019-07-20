#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CacheWall (Varnish)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Varnish')),
        self.matchHeader(('X-Varnish', '.+')),
        self.matchHeader(('X-Cachewall-Action', '.+?')),
        self.matchHeader(('X-Cachewall-Reason', '.+?')),
        self.matchContent(r'security.by.cachewall <.span>'),
        self.matchContent(r'403.naughty.+?not.nice!'),
        self.matchContent(r'varnish.cache.server')
    ]
    if any(i for i in schemes):
        return True
    return False