#!/usr/bin/env python


NAME = 'Wallarm (Wallarm Inc.)'


def is_waf(self):
    if self.matchheader(('Server', r'nginx.wallarm')):
        return True
    return False

