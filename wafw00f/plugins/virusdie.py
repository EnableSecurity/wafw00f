#!/usr/bin/env python


NAME = 'VirusDie (VirusDie LLC)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # Virusdie has lot of fingerprints in its blockpage
        if any(i in page for  i in (b'cdn.virusdie.ru/splash/firewallstop.png', b'copy; Virusdie.ru',
            b'Virusdie</title>')):
            return True
    return False