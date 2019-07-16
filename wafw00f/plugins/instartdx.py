#!/usr/bin/env python


NAME = 'Instart DX (Instart Logic)'


def is_waf(self):
    # Instart DX sometimes associates itself with these 3 separate headers.
    if self.matchheader(('X-Instart-Request-ID', '.+')):
        return True
    if self.matchheader(('X-Instart-Cache', '.+')):
        return True
    if self.matchheader(('X-Instart-WL', '.+')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if all(i in page for i in (b'The requested URL was rejected', b'Please consult with your administrator',
            b'Your support ID is:')):
            return True
    return False