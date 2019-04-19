#!/usr/bin/env python

NAME = 'Wallarm (Wallarm Inc.)'

def is_waf(self):
    if self.matchheader(('server', r"nginx\-wallarm")):
        return True
    return False

