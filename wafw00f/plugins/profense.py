#!/usr/bin/env python


NAME = 'Profense'


def is_waf(self):
    """
    Checks for server headers containing "profense"
    """
    return self.matchheader(('server', 'profense'))
