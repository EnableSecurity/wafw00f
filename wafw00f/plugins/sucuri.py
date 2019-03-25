#!/usr/bin/env python

"""
Homepage: https://sucuri.net
"""
NAME = 'Sucuri WAF'

def is_waf(self):
    """
    Checks for server headers containing "Sucuri"
    Example: `Server: Sucuri/Cloudproxy` (Happens on non HTTP 200 requests)
    """
    if self.matchheader(('server', 'Sucuri'))
      return True

    """
    Checks for headers containing "X-Sucuri-ID"
    Example: `x-sucuri-id: 13008` (case depends on HTTP status)
    """
    return self.matchheader(('X-Sucuri-ID', '.+'))
