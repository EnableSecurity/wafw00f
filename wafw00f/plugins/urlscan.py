#!/usr/bin/env python


NAME = 'URLScan (Microsoft)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, body = r
        # Most reliable fingerprint is this on block page
        if any(i in body for i in (b'Rejected-By-UrlScan', b'A custom filter or module, such as URLScan')):
            return True
    return False