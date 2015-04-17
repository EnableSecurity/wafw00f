#!/usr/bin/env python


NAME = 'IBM Web Application Security'


def is_waf(self):
    detected = False
    r = self.protectedfolder()
    if r is None:
        detected = True
    return detected
