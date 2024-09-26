#!/usr/bin/env python3


#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Kona SiteDefender (Akamai)'


def is_waf(self):
    if self.matchHeader(('Server', 'AkamaiGHost')):
        return True

    if self.matchHeader(('Server', 'AkamaiGHost'), attack=True)        :
        return True

    return False
