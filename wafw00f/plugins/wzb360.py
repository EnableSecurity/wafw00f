#!/usr/bin/env python


NAME = '360WangZhanBao (360 Technologies)'


def is_waf(self):
    if self.matchheader(('X-Powered-By-360WZB', '.+')):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, responsepage = r
        if response.status == 493 and b'/wzws-waf-cgi/' in responsepage:
            return True
        if b'wangshan.360.cn' in responsepage:
            return True
    return False