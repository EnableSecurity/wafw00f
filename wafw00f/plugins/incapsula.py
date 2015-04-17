#!/usr/bin/env python


NAME = 'Incapsula WAF'


def is_waf(self):
    # credit goes to Charlie Campbell
    if self.matchcookie('^.incap_ses'):
        return True
    if self.matchcookie('^visid.*='):
        return True
    return False
