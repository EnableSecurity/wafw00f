#!/usr/bin/env python


NAME = 'Kona Site Defender (Akamai)'


def is_waf(self):
    # Kona has a nice way of expressing itself in server header
    if self.matchheader(('Server', 'AkamaiGHost')):
        return True
    if self.matchheader(('Server', 'AkamaiGHost'), attack=True):
        return True
    return False