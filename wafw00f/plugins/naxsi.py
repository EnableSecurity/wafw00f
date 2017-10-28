#!/usr/bin/env python


NAME = 'Naxsi'
X_DATA_ORIGIN = 'X-Data-Origin'

def is_waf(self):
    if self.matchheader(('X-Data-Origin', 'naxsi/waf'), attack=False, ignorecase=True):
        return True
