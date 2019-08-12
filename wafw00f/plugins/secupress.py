#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'SecuPress WordPress Security (SecuPress)'


def is_waf(self):
    schema1 = [
        self.matchContent(r'<.+?>SecuPress<.+>'),
        self.matchStatus(503)
    ]
    schema2 = [
        self.matchContent(r'SecuPress<.+>'),
        self.matchContent(r'Block.ID.+?Bad.URL.Contents<.+?>')
    ]
    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    return False