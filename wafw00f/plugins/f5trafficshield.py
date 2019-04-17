#!/usr/bin/env python


NAME = 'Trafficshield (F5 Networks)'


def is_waf(self):
    if self.matchcookie(r'^ASINFO='):
        return True
    if self.matchheader(('Server', 'F5-TrafficShield')):
        return True
    return False