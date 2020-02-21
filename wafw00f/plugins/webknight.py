#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebKnight (AQTRONIX)'


def is_waf(self):
    schema1 = [
        self.matchStatus(999),
        self.matchReason('No Hacking')
    ]    
    schema2 = [
        self.matchStatus(404),
        self.matchReason('Hack Not Found')
    ]
    schema3 = [
        self.matchContent(r'WebKnight Application Firewall Alert'),
        self.matchContent(r'What is webknight\?'),
        self.matchContent(r'AQTRONIX WebKnight is an application firewall'),
        self.matchContent(r'WebKnight will take over and protect'),
        self.matchContent(r'aqtronix\.com/WebKnight'),
        self.matchContent(r'AQTRONIX.{0,10}?WebKnight'),
    ]
    if all(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True    
    if any(i for i in schema3):
        return True
    return False