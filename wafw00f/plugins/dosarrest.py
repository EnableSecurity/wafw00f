#!/usr/bin/env python


NAME = 'DOSarrest (DOSarrest Internet Security)'


def is_waf(self):
    if self.matchheader(('X-DIS-Request-ID', '.+')):
        return True
    # Found samples of DOSArrest returning 'Server: DoSArrest/3.5'
    if self.matchheader(('Server', 'DOSarrest(.*)?')):
        return True
    return False