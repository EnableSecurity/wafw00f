#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
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

    return False
