#!/usr/bin/env python


NAME = 'DOSarrest'


def is_waf(self):
    if self.matchheader(('X-DIS-Request-ID', '.+')):
        return True
    if self.matchheader(('Server', 'DOSarrest')):
        return True
    return False