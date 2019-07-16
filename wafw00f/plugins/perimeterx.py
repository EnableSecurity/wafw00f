#!/usr/bin/env python


NAME = 'PerimeterX (PerimeterX)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if any(i in page for i in (b'www.perimeterx.com/whywasiblocked', b'client.perimeterx.net', 
            b'Access to this page has been denied because we believe you are using automation tools')):
            return True
    return False