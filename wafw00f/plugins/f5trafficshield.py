#!/usr/bin/env python


NAME = 'F5 Trafficshield'


def is_waf(self):
    for hv in [['cookie', '^ASINFO='], ['server', 'F5-TrafficShield']]:
        r = self.matchheader(hv)
        if r is None:
            return
        elif r:
            return r
    # the following based on nmap's http-waf-fingerprint.nse
    if self.matchheader(('server', 'F5-TrafficShield')):
        return True
    return False
