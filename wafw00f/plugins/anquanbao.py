#!/usr/bin/env python


NAME = 'Anquanbao'


def is_waf(self):
    return self.matchheader(('X-Powered-By-Anquanbao', '.+'))
