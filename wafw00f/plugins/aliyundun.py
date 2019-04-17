#!/usr/bin/env python


NAME = 'AliYunDun (Alibaba Cloud Computing)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        if response.status == 405 and b'errors.aliyun.com' in page:
            return True
    return False