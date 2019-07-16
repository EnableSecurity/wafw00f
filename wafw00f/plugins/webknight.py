#!/usr/bin/env python


NAME = 'WebKnight (AQTRONIX)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        # This method is obsolete now. Sites using older versions of
        # Webknight will only return this fingerprint
        if response.status == 999 and response.reason == 'No Hacking':
            return True
        # Nowadays updated version of Webknight return this
        if response.status == 404 and response.reason == 'Hack Not Found':
            return True
        if any(i in page for i in (b'WebKnight Application Firewall Alert', b'What is WebKnight?',
            b'AQTRONIX WebKnight is an application firewall', b'WebKnight will take over and protect',
            b'aqtronix.com/WebKnight', b'>AQTRONIX</FONT> WebKnight')):
            return True
    return False
