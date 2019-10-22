#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Xuanwudun'


def is_waf(self):
    schemes = [
        self.matchContent(r"admin\.dbappwaf\.cn/(index\.php/Admin/ClientMisinform/)?"),
        self.matchContent(r'class=.(db[\-_]?)?waf(.)?([\-_]?row)?>')
    ]
    if any(i for i in schemes):
        return True
    return False