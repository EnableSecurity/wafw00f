#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Xuanwudun (Xuanwudun)'


def is_waf(self):
    if self.matchContent(r"admin\.dbappwaf\.cn/(index\.php/Admin/ClientMisinform/)?"):
        return True

    if self.matchContent(r'class=.(db[\-_]?)?waf(.)?([\-_]?row)?>'):
        return True

    return False
