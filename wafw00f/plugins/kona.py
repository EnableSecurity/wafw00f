#!/usr/bin/env python


#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Kona Site Defender (Akamai)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'AkamaiGHost')),
        self.matchHeader(('Server', 'AkamaiGHost'), attack=True)        
    ]
    if any(i for i in schemes):
        return True
    return False