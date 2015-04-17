#!/usr/bin/env python


NAME = '360WangZhanBao'


def is_waf(self):
    return self.matchheader(('X-Powered-By-360WZB', '.+'))
