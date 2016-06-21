#!/usr/bin/env python


NAME = 'IBM Web Application Security'


def is_waf(self):
    normal = self.normalrequest()
    protected = self.protectedfolder()

    return protected is None and normal is not None
