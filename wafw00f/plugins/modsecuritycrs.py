#!/usr/bin/env python


NAME = 'ModSecurity (OWASP CRS)'


def is_waf(self):
    r = self.request('GET', self.path + '?id=' + self.xssstring)
    normal = self.normalrequest()

    if r is None or normal is None:
        return False

    response, _ = r
    normalresponse, _ = normal

    return normalresponse.status != response.status
