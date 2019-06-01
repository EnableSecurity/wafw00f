#!/usr/bin/env python


NAME = 'Sabre Firewall (Sabre)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsepage = r
        if any(i in responsepage for i in (b'dxsupport@sabre.com', b'<title>Application Firewall Error</title>',
            b'email link will automatically add some important details to the email for us to investigate')):
            return True
    return False