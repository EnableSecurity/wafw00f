#!/usr/bin/env python


NAME = 'PowerCDN'


def is_waf(self):
    # More later versions of PowerCDN waf >= v4.x return these two headers specifically.
    # X-Cache: HIT from cc89.powercdn.com
    # Via: 1.1 cc89.powercdn.com (PowerCDN/4.1)
    # I implemented them in this way:
    if self.matchheader(('Via', '(.*)?powercdn.com(.*)?')):
        return True
    if self.matchheader(('X-Cache', '(.*)?powercdn.com(.*)?')):
        return True
    # This used be found on earlier versions of PowerCDN no longer now. 
    if self.matchheader(('PowerCDN', '.+')):
        return True
    
    return False