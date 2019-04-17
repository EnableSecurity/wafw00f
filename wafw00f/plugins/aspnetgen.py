#!/usr/bin/env python


NAME = 'ASP.NET Generic Web Application Protection'


def is_waf(self):
    detected1 = False
    detected2 = False
    # So first we are checking for whether the site is running ASP.NET or not
    if self.matchheader(('X-Powered-By', r'ASP.NET(.*)?')):
        detected1 = True
    # Sites running ASP.NEt also sometimes return this header
    if self.matchheader(('X-ASPNET-Version', '.*')):
        detected1 = True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'This generic 403 error means that the authenticated user is not authorized to use the requested resource', b'request could not be understood', b'potentially dangerous request querystring')):
            detected2 = True
    # We return whatever we got from those 3 checks
    if detected1 and detected2:
        return True
    return False