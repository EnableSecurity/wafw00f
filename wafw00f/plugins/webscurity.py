#!/usr/bin/env python


NAME = 'Juniper WebApp Secure'


def is_waf(self):
    detected = False
    r = self.normalrequest()
    if r is None:
        return
    response, responsebody = r
    if response.status == 403:
        return detected
    newpath = self.path + '?nx=@@'
    r = self.request(path=newpath)
    if r is None:
        return
    response, responsebody = r
    if response.status == 403:
        detected = True
    return detected
