#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CacheWall (Varnish)'


def is_waf(self):
    if self.matchHeader(('Server', 'Varnish')):
        return True

    if self.matchHeader(('X-Varnish', '.+')):
        return True

    if self.matchHeader(('X-Cachewall-Action', '.+?')):
        return True

    if self.matchHeader(('X-Cachewall-Reason', '.+?')):
        return True

    if self.matchContent(r'security by cachewall'):
        return True

    if self.matchContent(r'403 naughty.{0,10}?not nice!'):
        return True

    if self.matchContent(r'varnish cache server'):
        return True

    return False
