#!/usr/bin/env python


NAME = 'SecuPress WordPress Security (SecuPress)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        if response.status == 503 and b'<h1>SecuPress</h1><h2>' in page:
            return True
        if all(i in page for i in (b'SecuPress</h1>', b'Block ID: Bad URL Contents</p>')):
            return True
    return False