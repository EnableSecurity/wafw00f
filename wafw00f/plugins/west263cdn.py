#!/usr/bin/env python


NAME = 'West263CDN'


def is_waf(self):
    return self.matchheader(('X-Cache', '.+WT263CDN-.+'))
