#!/usr/bin/env python


NAME = 'BinarySec'


def is_waf(self):
    if self.matchheader(('server', 'BinarySec')):
        return True
    elif self.matchheader(('x-binarysec-via', '.')):
        return True
    elif self.matchheader(('x-binarysec-nocache', '.')):
        return True
    else:
        return False
