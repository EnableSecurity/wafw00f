#!/usr/bin/env python

NAME = 'Edgecast (Verizon Digital Media)'

def is_waf(self):
    if self.matchheader(('Server', '^ECD \\(.*?\\)$')):
        return True
    if self.matchheader(('Server', '^ECS \\(.*?\\)$')):
        return True
    return False