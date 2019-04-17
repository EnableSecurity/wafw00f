#!/usr/bin/env python


NAME = 'BinarySec (BinarySec)'


def is_waf(self):
    if self.matchheader(('server', 'BinarySec')):
        return True
    if self.matchheader(('x-binarysec-via', '.+')):
        return True
    if self.matchheader(('x-binarysec-nocache', '.+')):
        return True
    return False