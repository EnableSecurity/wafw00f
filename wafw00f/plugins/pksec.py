#!/usr/bin/env python


NAME = 'pkSecurity Intrusion Detection System'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Most reliable fingerprints first
        if all(i in page for i in (b'pkSecurityModule', b'Security Alert')):
            return True
        # Group 1 Fingerprints id 1b65rtt
        if any(i in page for i in (b'A safety-critical call was detected and blocked!', 
            b'A safety critical request was discovered and blocked!')):
            return True
        # Group 2 Fingerprints id 1b65r0x
        if any(i in page for i in (b'As this could be a potential hack attack, the access to this site was blocked.',
            b'You have exceeded the maximum number of reloads per minute and prevented access to this page!')):
            return True
    return False