#!/usr/bin/env python

NAME = 'Comodo WAF'

def is_waf(self):
    # The (.*)? was required since some servers return additional info like
    # version of the WAF. eg. Protected by COMODO WAF mod_fcgid/2.3.9   
    if self.matchheader(('server', "Protected by COMODO WAF(.*)?")):
        return True
    return False