#!/usr/bin/env python


NAME = 'Expression Engine (EllisLab)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r
        # There are traces found where cookie is returning values like:
        # Set-Cookie: exp_last_query=834y8d73y94d8g983u4shn8u4shr3uh3
        # Set-Cookie: exp_last_id=b342b432b1a876r8
        if response.getheader('Set-Cookie'):
            if 'exp_last_' in response.getheader('Set-Cookie'):
                return True
        # In-page fingerprints vary a lot in different sites. Hence these are not quite reliable.
        if any(i in page for i in (b'Invalid GET Data', b'Invalid URI')):
            return True
    return False