#!/usr/bin/env python


NAME = 'F5 Trafficshield'


def is_waf(self):
    if self.matchcookie('^ASINFO='):
        return True
    if self.matchheader(('server', 'F5-TrafficShield')):
        return True
    return False