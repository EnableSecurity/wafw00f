#!/usr/bin/env python

NAME = 'AdNovum nevisProxy'

def is_waf(self):
    return self.matchcookie('^Navajo.*?$')
