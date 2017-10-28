#!/usr/bin/env python


NAME = 'Radware'


def is_waf(self):
    # credit goes to W3AF
    if self.matchheader(('X-SL-CompState', '.')):
        return True
