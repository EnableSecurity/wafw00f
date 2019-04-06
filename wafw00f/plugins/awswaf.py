#!/usr/bin/env python

NAME = 'AWS WAF'

def is_waf(self):
    # Prioritize these checks first which doesn't require attack
    if self.matchheader(('X-AMZ-ID', '.*')):
        return True
    if self.matchheader(('X-AMZ-Request-ID', '.*')):
        return True
    # Move to attack phase for identification
    if self.matchheader(('Server', 'awselb/2\\.0'), attack=True):
        return True
    return False