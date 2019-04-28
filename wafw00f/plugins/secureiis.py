#!/usr/bin/env python


NAME = 'eEye SecureIIS (BeyondTrust)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsebody = r
        # Most reliable fingerprint is this on block page
        if any(i in responsebody for i in (b'SecureIIS is an internet security application', 
            b'Download SecureIIS Personal Edition', b'http://www.eeye.com/SecureIIS/')):
            return True
    return False