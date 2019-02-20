#!/usr/bin/env python


NAME = 'NSFocus'


def is_waf(self):
    return self.matchheader(('server', 'NSFocus'))
