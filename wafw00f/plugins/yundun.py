#!/usr/bin/env python


NAME = 'Yundun (Yundun)'


def is_waf(self):
    # Yundun has its own server header set
    if self.matchheader(('Server', 'YUNDUN')):
        return True
    #  X-Cache too sometimes
    if self.matchheader(('X-Cache', 'YUNDUN')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Yundun has its nice characteristic blockpage
        if any(i in page for  i in (b'Blocked by YUNDUN Cloud WAF', b'yundun.com/yd_http_error/')):
            return True
    return False