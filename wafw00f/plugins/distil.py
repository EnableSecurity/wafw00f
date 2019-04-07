#!/usr/bin/env python


NAME = 'Distil Networks'


def is_waf(self):
    if self.matchcookie('crawlprotecttag'):
        return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Distil exposes itself in its captchas, and picture on blockpage
        if any(i in page for i in (b'cdn.distilnetworks.com/images/anomaly-detected.png',
            b'distilCaptchaForm', b'distilCallbackGuard')):
            return True
    return False