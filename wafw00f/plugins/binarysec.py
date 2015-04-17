#!/usr/bin/env python


NAME = 'BinarySec'


def is_waf(self):
    # credit goes to W3AF
    if self.matchheader(('server', 'BinarySec')):
        return True
    # the following based on nmap's http-waf-fingerprint.nse
    elif self.matchheader(('x-binarysec-via', '.')):
        return True
    # the following based on nmap's http-waf-fingerprint.nse
    elif self.matchheader(('x-binarysec-nocache', '.')):
        return True
    else:
        return False
