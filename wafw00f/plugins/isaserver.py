#!/usr/bin/env python


NAME = 'Microsoft ISA Server'


def is_waf(self):
    detected = False
    r = self.invalidhost()
    if r is None:
        return
    response, responsebody = r
    if response.reason in self.isaservermatch:
        detected = True
    return detected
