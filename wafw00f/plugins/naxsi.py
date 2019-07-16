#!/usr/bin/env python


NAME = 'NAXSI (NBS Systems)'


def is_waf(self):
	# Sometimes naxsi waf returns 'x-data-origin: naxsi/waf'
    if self.matchheader(('X-Data-Origin', r'^naxsi(.*)?')):
    	return True
    # Found samples returning 'server: naxsi/2.0'
    if self.matchheader(('server', r'naxsi(.*)?')):
    	return True
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, responsebody = r
        if any(i in responsebody for i in (b'Blocked By NAXSI', b'Naxsi Blocked Information')):
            return True
    return False