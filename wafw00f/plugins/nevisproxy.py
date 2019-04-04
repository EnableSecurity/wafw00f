#!/usr/bin/env python

NAME = 'AdNovum nevisProxy'

def is_waf(self):
    if self.matchcookie('^Navajo.*?$'):
        return True
    return False