#!/usr/bin/env python


NAME = 'eEye Digital Security SecureIIS'


def is_waf(self):
    # credit goes to W3AF
    detected = False
    r = self.normalrequest()
    if r is None:
        return
    response, responsebody = r
    if response.status == 404:
        return
    headers = dict()
    headers['Transfer-Encoding'] = 'z' * 1025
    r = self.normalrequest(headers=headers)
    if r is None:
        return
    response, responsebody = r
    if response.status == 404:
        detected = True
    return detected
