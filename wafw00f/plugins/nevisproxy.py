#!/usr/bin/env python

NAME = 'AdNovum nevisProxy'

def is_waf(self):
    # credit goes to an anonymous reporter
    return self.matchcookie('^Navajo.*?$')
