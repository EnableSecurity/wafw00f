#!/usr/bin/env python

NAME = 'Edgecast / Verizon Digital media'

def is_waf(self):
    return self.matchheader(('Server', '^ECD \(.*?\)$')) or self.matchheader(('Server', '^ECS \(.*?\)$'))
