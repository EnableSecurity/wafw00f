#!/usr/bin/env python


NAME = 'Edgecast (Verizon Digital Media)'


def is_waf(self):
    if self.matchheader(('Server', r'^ECD(.*)?')):
        return True
    if self.matchheader(('Server', r'^ECS(.*)?')):
        return True
    return False