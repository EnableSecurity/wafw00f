#!/usr/bin/env python


NAME = 'Microsoft ISA Server'



def is_waf(self):
    isaservermatch = [
        'Forbidden ( The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.  )',
        'Forbidden ( The ISA Server denied the specified Uniform Resource Locator (URL)'
    ]
    detected = False
    r = self.invalidhost()
    if r is None:
        return
    response, _ = r
    if response.reason in isaservermatch:
        detected = True
    return detected
