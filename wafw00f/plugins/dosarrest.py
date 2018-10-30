#!/usr/bin/env python


NAME = 'DOSarrest'


def is_waf(self):
    return self.matchheader(('X-DIS-Request-ID', '.+')) or self.matchheader(('server', 'DOSarrest'))