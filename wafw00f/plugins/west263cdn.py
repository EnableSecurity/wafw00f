#!/usr/bin/env python


NAME = 'West263CDN'


def is_waf(self):
	# Found traces where only WT263CDN was in X-Cache header
    if self.matchheader(('X-Cache', r'(.*)?WT263CDN(.*)?')):
        return True
    return False
