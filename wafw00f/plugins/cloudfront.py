#!/usr/bin/env python
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudfront (Amazon)'


def is_waf(self):
    # This is standard detection schema, checking the server header
    if self.matchHeader(('Server', 'Cloudfront')):
        return True

    # Found samples returning 'Via: 1.1 58bfg7h6fg76h8fg7jhdf2.cloudfront.net (CloudFront)'
    if self.matchHeader(('Via', r'([0-9\.]+?)? \w+?\.cloudfront\.net \(Cloudfront\)')):
        return True

    # The request token is sent along with this header, eg:
    # X-Amz-Cf-Id: sX5QSkbAzSwd-xx3RbJmxYHL3iVNNyXa1UIebDNCshQbHxCjVcWDww==
    if self.matchHeader(('X-Amz-Cf-Id', '.+?'), attack=True):
        return True

    # This is another reliable fingerprint found on headers
    if self.matchHeader(('X-Cache', 'Error from Cloudfront'), attack=True):
        return True

    # These fingerprints are found on the blockpage itself
    if self.matchContent(r'Generated by cloudfront \(CloudFront\)'):
        return True

    return False
