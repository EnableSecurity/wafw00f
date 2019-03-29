#!/usr/bin/env python


NAME = 'West263CDN'


def is_waf(self):
	# Found traces where only WT263CDN was in X-Cache header
    return self.matchheader(('X-Cache', '(.*)?WT263CDN(.*)?'))
