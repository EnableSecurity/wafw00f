#!/usr/bin/env python


NAME = 'Microsoft URLScan'


def is_waf(self):
    detected = False
    testheaders = dict()
    testheaders['Translate'] = 'z' * 10
    testheaders['If'] = 'z' * 10
    testheaders['Lock-Token'] = 'z' * 10
    testheaders['Transfer-Encoding'] = 'z' * 10
    r = self.normalrequest()
    if r is None:
        return
    response, _tmp = r
    r = self.normalrequest(headers=testheaders)
    if r is None:
        return
    response2, _tmp = r
    if response.status != response2.status:
        if response2.status == 404:
            detected = True
    return detected
