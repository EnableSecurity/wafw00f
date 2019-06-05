#!/usr/bin/env python


NAME = 'West263 Content Delivery Network'


def is_waf(self):
	# Found traces where only WT263CDN was in X-Cache header
    # Also found traces where X-Cache header where WST263CDN was being put
    if self.matchheader(('X-Cache', r'(.+)?W(S)?T263CDN(.+)?')):
        return True
    return False
