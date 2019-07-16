#!/usr/bin/env python


NAME = 'AWS Elastic Load Balancer (Amazon)'


def is_waf(self):
    # Prioritize these checks first which doesn't require attack
    if self.matchheader(('X-AMZ-ID', '.*')):
        return True
    if self.matchheader(('X-AMZ-Request-ID', '.*')):
        return True
    if self.matchcookie(r'^aws.?alb='):
        return True
    # Move to attack phase for identification
    if self.matchheader(('Server', r'awselb/2\.0'), attack=True):
        return True
    return False