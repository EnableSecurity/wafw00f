#!/usr/bin/env python


NAME = 'DynamicWeb Injection Check (DynamicWeb)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, _ = r
        # The reason why both dashes and underscores are put to check,
        # because this is a module which can be renamed easily.
        # So a user can manipulate the name easily. These two instances
        # are the ones which I have observed in the wild most commonly.
        if response.getheader('X-403-Status-By') == 'dw-inj-check':
            return True
        if response.getheader('X-403-Status-By') == 'dw_inj_check':
            return True
    return False