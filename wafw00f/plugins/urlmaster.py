#!/usr/bin/env python


NAME = 'URLMaster SecurityCheck (iFinity/DotNetNuke)'


def is_waf(self):
    # URLMaster sometimes associates itself with these 2 separate headers.
    # This one for debug more enabled on ASPX 4.x versions.
    if self.matchheader(('X-UrlMaster-Debug', '.+')):
        return True
    if self.matchheader(('X-UrlMaster-Ex', '.+')):
        return True
    # Now going for attack phase
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        # This often displayed when the debug mode is enabled.
        # Otherwise it is the regular 403vblockpage itself.
        if all(i in page for i in (b'UrlRewriteModule', b'SecurityCheck')):
            return True
    return False