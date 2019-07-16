#!/usr/bin/env python


NAME = 'Anquanbao (Anquanbao)'


def is_waf(self):
    if self.matchheader(('X-Powered-By-Anquanbao', '.+')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        # Anquanbao returns 405 and has reference to /aqb_cc/error/
        # in its block page
        if response.status == 405 and b'aqb_cc/error/' in page:
            return True
    return False