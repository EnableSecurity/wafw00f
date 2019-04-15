#!/usr/bin/env python


NAME = 'Xuanwudun'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # The only unique fingerprint I found on their block page is this
        if b'admin.dbappwaf.cn/index.php/Admin/ClientMisinform/' in page:
            return True
    return False