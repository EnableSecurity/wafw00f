#!/usr/bin/env python


NAME = 'Citrix NetScaler'


def is_waf(self):
    """
    First checks if a cookie associated with Netscaler is present,
    if not it will try to find if a "Cneonction" or "nnCoection" is returned
    for any of the attacks sent
    """
    # NSC_ and citrix_ns_id come from David S. Langlands <dsl 'at' surfstar.com>
    if self.matchcookie('^(ns_af=|citrix_ns_id|NSC_)'):
        return True
    if self.matchheader(('Cneonction', 'close'), attack=True):
        return True
    if self.matchheader(('nnCoection', 'close'), attack=True):
        return True
    if self.matchheader(('Via', 'NS-CACHE'), attack=True):
        return True
    if self.matchheader(('x-client-ip', '.'), attack=True):
        return True
    if self.matchheader(('Location', '\/vpn\/index\.html')):
        return True
    if self.matchcookie('^pwcount'):
        return True
    return False
