#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AWS Elastic Load Balancer (Amazon)'


def is_waf(self):
    if self.matchHeader(('X-AMZ-ID', '.+?')):
        return True

    if self.matchHeader(('X-AMZ-Request-ID', '.+?')):
        return True

    if self.matchCookie(r'^aws.?alb='):
        return True

    if self.matchHeader(('Server', r'aws.?elb'), attack=True):
        return True

    if self.matchHeader(('X-Blocked-By-WAF', 'Blocked_by_custom_response_for_AWSManagedRules.*')):
        return True

    return False
