#!/usr/bin/env python


NAME = 'Barracuda Application Firewall'


def is_waf(self):
    # credit goes to W3AF
    if self.matchcookie('^barra_counter_session='):
        return True
    # credit goes to Charlie Campbell
    if self.matchcookie('^BNI__BARRACUDA_LB_COOKIE='):
        return True
    # credit goes to yours truly
    if self.matchcookie('^BNI_persistence='):
        return True
    if self.matchcookie('^BN[IE]S_.*?='):
        return True
    return False
