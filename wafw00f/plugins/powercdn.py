#!/usr/bin/env python


NAME = 'PowerCDN (PowerCDN)'


def is_waf(self):
    # More later versions of PowerCDN waf >= v4.x return these two headers specifically.
    # I implemented them in this way:
    # Via: 1.1 cc89.powercdn.com (PowerCDN/4.1)
    if self.matchheader(('Via', r'(.*)?powercdn.com(.*)?')):
        return True
    # X-Cache: HIT from cc89.powercdn.com
    if self.matchheader(('X-Cache', r'(.*)?powercdn.com(.*)?')):
        return True
    # This used be found on earlier versions of PowerCDN no longer now. 
    if self.matchheader(('PowerCDN', '.+')):
        return True
    
    return False