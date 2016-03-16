#!/usr/bin/env python


NAME = 'ModSecurity (OWASP CRS)'


def is_waf(self):
    detected = False
    r = self.request('GET', '/?id=' + self.xssstring)
    if r is None:
        return False

    normalresponse, _ = self.normalrequest()
    response, _ = r

    return normalresponse.status != response.status
